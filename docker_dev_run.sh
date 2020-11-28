#!/bin/bash

docker run --rm -td -v `pwd`:/app --name bot --entrypoint bash bot
