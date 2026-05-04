"""
Helper Functions for Movie Poster Visual Feature Analysis
==========================================================

This module provides utility functions for extracting visual features
from movie poster images and analyzing their relationship to box office revenue.

Author: Rowan Rosenblum, UVA DS4002
Date: Spring 2025
"""

import os
import time
import requests
import numpy as np
import pandas as pd
import cv2
from PIL import Image
from sklearn.cluster import KMeans


# =============================================================================
# POSTER DOWNLOAD
# =============================================================================

def download_poster(tconst, api_key, save_dir="posters/", size="w500"):
    """
    Download a movie poster from TMDB using its IMDB tconst ID.
    
    Parameters
    ----------
    tconst : str
        IMDB identifier (e.g., 'tt1234567')
    api_key : str
        Your TMDB API key
    save_dir : str
        Directory to save poster images
    size : str
        TMDB image size (default 'w500')
        
    Returns
    -------
    str or None
        Path to the saved image, or None if download failed
    """
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{tconst}.jpg")
    
    if os.path.exists(save_path):
        return save_path
    
    try:
        # Look up the TMDB movie ID from the IMDB tconst
        find_url = f"https://api.themoviedb.org/3/find/{tconst}"
        params = {"api_key": api_key, "external_source": "imdb_id"}
        resp = requests.get(find_url, params=params, timeout=10)
        resp.raise_for_status()
        
        results = resp.json().get("movie_results", [])
        if not results:
            return None
        
        poster_path = results[0].get("poster_path")
        if not poster_path:
            return None
        
        # Download the poster image
        img_url = f"https://image.tmdb.org/t/p/{size}{poster_path}"
        img_resp = requests.get(img_url, timeout=15)
        img_resp.raise_for_status()
        
        with open(save_path, "wb") as f:
            f.write(img_resp.content)
        
        # Rate limiting: TMDB allows ~40 requests per 10 seconds
        time.sleep(0.3)
        return save_path
    
    except Exception as e:
        print(f"  Error downloading {tconst}: {e}")
        return None


# =============================================================================
# COLOR FEATURE EXTRACTION
# =============================================================================

def get_dominant_colors(image_path, k=5):
    """
    Extract the k most dominant colors from an image using K-Means clustering.
    
    Parameters
    ----------
    image_path : str
        Path to the image file
    k : int
        Number of color clusters (default 5)
        
    Returns
    -------
    tuple
        (dominant_rgb, all_centroids, labels)
        - dominant_rgb: (R, G, B) tuple for the most common color
        - all_centroids: array of shape (k, 3) with all cluster centers
        - labels: cluster label for each pixel
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")
    
    # Convert BGR -> RGB and reshape to a list of pixels
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixels = img_rgb.reshape(-1, 3).astype(np.float32)
    
    # Run K-Means
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(pixels)
    
    # Find the largest cluster (most dominant color)
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant_idx = labels[np.argmax(counts)]
    dominant_rgb = kmeans.cluster_centers_[dominant_idx].astype(int)
    
    return tuple(dominant_rgb), kmeans.cluster_centers_, kmeans.labels_


def compute_brightness_saturation(image_path):
    """
    Compute the average brightness and saturation of an image.
    
    Parameters
    ----------
    image_path : str
        Path to the image file
        
    Returns
    -------
    tuple
        (avg_brightness, avg_saturation) as floats in range 0-255
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    avg_saturation = float(np.mean(hsv[:, :, 1]))
    avg_brightness = float(np.mean(hsv[:, :, 2]))
    
    return avg_brightness, avg_saturation


def compute_orange_teal_score(image_path):
    """
    Compute the proportion of pixels that fall in orange or teal hue ranges.
    
    This captures the prevalence of the popular Hollywood "orange and teal"
    color grading style.
    
    Parameters
    ----------
    image_path : str
        Path to the image file
        
    Returns
    -------
    float
        Score between 0 and 1, where 1 means all pixels are orange or teal
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = hsv[:, :, 0]  # OpenCV hue range: 0-180
    
    # Orange hue range (~10-25 on the 0-180 scale)
    orange_mask = (hue >= 10) & (hue <= 25)
    # Teal hue range (~80-100 on the 0-180 scale)
    teal_mask = (hue >= 80) & (hue <= 100)
    
    total_pixels = hue.size
    ot_pixels = np.sum(orange_mask) + np.sum(teal_mask)
    
    return float(ot_pixels / total_pixels)


# =============================================================================
# FACE DETECTION
# =============================================================================

def count_faces(image_path, use_retinaface=True):
    """
    Count the number of faces in an image.
    
    Parameters
    ----------
    image_path : str
        Path to the image file
    use_retinaface : bool
        If True, use RetinaFace (more accurate, requires tensorflow).
        If False, use OpenCV's Haar cascade (faster, less accurate).
        
    Returns
    -------
    int
        Number of faces detected
    """
    if use_retinaface:
        try:
            from retinaface import RetinaFace
            faces = RetinaFace.detect_faces(image_path)
            if isinstance(faces, dict):
                return len(faces)
            return 0
        except ImportError:
            print("RetinaFace not installed. Falling back to Haar cascade.")
    
    # Fallback: OpenCV Haar cascade
    img = cv2.imread(image_path)
    if img is None:
        return 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return len(faces)


def compute_face_density(image_path, face_count=None):
    """
    Compute face density: (face_count / total_pixels) * 10,000.
    
    Parameters
    ----------
    image_path : str
        Path to the image file
    face_count : int or None
        Pre-computed face count. If None, will detect faces automatically.
        
    Returns
    -------
    float
        Face density metric
    """
    if face_count is None:
        face_count = count_faces(image_path)
    
    img = cv2.imread(image_path)
    if img is None:
        return 0.0
    
    total_pixels = img.shape[0] * img.shape[1]
    return (face_count / total_pixels) * 10000


# =============================================================================
# COMBINED EXTRACTION
# =============================================================================

def extract_all_features(image_path, use_retinaface=True):
    """
    Extract all visual features from a single poster image.
    
    Parameters
    ----------
    image_path : str
        Path to the poster image
    use_retinaface : bool
        Whether to use RetinaFace for face detection
        
    Returns
    -------
    dict
        Dictionary containing all extracted features:
        - dom_r, dom_g, dom_b: dominant color RGB values
        - avg_brightness: mean pixel brightness
        - avg_saturation: mean pixel saturation
        - orange_teal_score: proportion of orange/teal pixels
        - face_count: number of detected faces
        - face_density: faces per 10,000 pixels
    """
    features = {}
    
    # Dominant color
    dominant_rgb, _, _ = get_dominant_colors(image_path, k=5)
    features["dom_r"] = int(dominant_rgb[0])
    features["dom_g"] = int(dominant_rgb[1])
    features["dom_b"] = int(dominant_rgb[2])
    
    # Brightness and saturation
    brightness, saturation = compute_brightness_saturation(image_path)
    features["avg_brightness"] = round(brightness, 2)
    features["avg_saturation"] = round(saturation, 2)
    
    # Orange-teal score
    features["orange_teal_score"] = round(
        compute_orange_teal_score(image_path), 4
    )
    
    # Face detection
    fc = count_faces(image_path, use_retinaface=use_retinaface)
    features["face_count"] = fc
    features["face_density"] = round(
        compute_face_density(image_path, face_count=fc), 4
    )
    
    return features


# =============================================================================
# RELEASE WINDOW CLASSIFICATION
# =============================================================================

def classify_release_window(month):
    """
    Classify a release month into a release window category.
    
    Parameters
    ----------
    month : int
        Release month (1-12)
        
    Returns
    -------
    str
        One of 'Summer', 'Holiday', 'Spring', or 'Other'
    """
    if month in [5, 6, 7]:
        return "Summer"
    elif month in [11, 12]:
        return "Holiday"
    elif month in [3, 4]:
        return "Spring"
    else:
        return "Other"


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    print("Movie Poster Feature Extraction Helper Functions")
    print("=" * 50)
    print("Import this module in your Jupyter notebook:")
    print()
    print("  from helper_functions import extract_all_features")
    print("  features = extract_all_features('poster.jpg')")
    print()
    print("Available functions:")
    print("  - download_poster(tconst, api_key)")
    print("  - get_dominant_colors(image_path, k=5)")
    print("  - compute_brightness_saturation(image_path)")
    print("  - compute_orange_teal_score(image_path)")
    print("  - count_faces(image_path)")
    print("  - compute_face_density(image_path)")
    print("  - extract_all_features(image_path)")
    print("  - classify_release_window(month)")
