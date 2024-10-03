#!/bin/bash

echo "Stopping Kafka with Homebrew..."
brew services stop kafka

echo "Stopping Zookeeper with Homebrew..."
brew services stop zookeeper

echo "Zookeeper and Kafka have been stopped."
