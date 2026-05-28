#!/usr/bin/env bash
# One-time setup: deploy nginx slides container to VPS.
# Run from the project root: bash hosting/setup-vps.sh

set -e

VPS="root@178.105.51.174"
REMOTE="/root/slides-hosting"

echo "→ Creating directories on VPS"
ssh "$VPS" "mkdir -p /root/slides $REMOTE"

echo "→ Copying Docker config"
scp hosting/Dockerfile hosting/docker-compose.yml hosting/nginx.conf "$VPS:$REMOTE/"

echo "→ Building and starting container"
ssh "$VPS" "cd $REMOTE && docker compose up -d --build"

echo "→ Verifying container is running"
ssh "$VPS" "docker ps | grep slides"

echo ""
echo "✓ Container running. Will be accessible at http://178.105.51.174:8080/ after first push."
echo "  Run: python scripts/push.py"
