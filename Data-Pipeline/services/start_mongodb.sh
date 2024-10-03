#!/bin/bash

echo "Adding GG Credentials..."
export GOOGLE_APPLICATION_CREDENTIALS="/Users/kys1kh6n9dau/Documents/project-finance-400806-eca0ec4df29d.json"
echo "Credentials added."

echo "Starting MongoDB..."
mongod --dbpath /usr/local/var/mongodb
echo "MongoDB have been initialized."
