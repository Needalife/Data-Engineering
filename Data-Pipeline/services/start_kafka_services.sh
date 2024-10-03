#!/bin/bash

echo "Starting Zookeeper /w Homebrew..."
brew services start zookeeper

sleep 3

echo "Starting Kafka /w Homebrew..."
brew services start kafka

echo "Zookeeper and Kafka have been started."
