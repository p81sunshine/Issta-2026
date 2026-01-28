#!/bin/bash
# 实时监控训练过程资源使用情况

echo "开始监控训练进程资源使用 (按Ctrl+C停止)..."
echo "========================================================"

watch -n 5 '
echo "时间: $(date +"%Y-%m-%d %H:%M:%S")"
echo "----------------------------------------"
echo "系统负载:"
uptime
echo ""
echo "内存使用 (GB):"
free -g
echo ""
echo "僵尸进程数: $(ps aux | grep "Z" | grep -v grep | wc -l)"
echo "Ray进程数: $(ps aux | grep "ray::" | grep -v grep | wc -l)" 
echo "训练进程数: $(pgrep -f "train_agent_ppo" | wc -l)"
echo ""
echo "Top 5 CPU占用进程:"
ps aux --sort=-%cpu | head -6
echo ""
echo "Top 5 内存占用进程:"
ps aux --sort=-%mem | head -6
'




































