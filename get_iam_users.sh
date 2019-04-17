#!/bin/bash
aws iam list-users | awk -F 'user/' '{ print $2}'| awk '{print $1}'
