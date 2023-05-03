#!/bin/bash

echo "*************************************************************"
echo "* Installing packages using apt"
echo "*************************************************************"
sudo apt-get update
echo "*"
echo "* - Installing tesseract-ocr..."
echo "*"
sudo apt-get -y install tesseract-ocr
echo "*"
echo "* - Installing libtesseract-dev..."
echo "*"
sudo apt-get -y install libtesseract-dev
echo "*"
echo "* - Installing poppler-utils..."
echo "*"
sudo apt-get -y install poppler-utils

echo "*************************************************************"
echo "* Installing python requirements"
echo "*************************************************************"

pip install -r requirements.txt
