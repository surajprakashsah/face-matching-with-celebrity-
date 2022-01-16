# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:47:24 2022

@author: suraj sah
"""
from bing_image_downloader import downloader

downloader.download('suraj prakash sah', limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)