#!/bin/bash
ps faux | grep -w wineboot | grep -v grep | awk '{print $2}'     | while read -r pid; do kill -9 $pid; done
ps faux | grep pressure-vessel | grep -v grep | awk '{print $2}' | while read -r pid; do kill -9 $pid; done
ps faux | grep 'C:\\windows\\' | grep -v grep | awk '{print $2}' | while read -r pid; do kill -9 $pid; done
ps faux | grep ge-proton | grep -v grep | awk '{print $2}' | while read -r pid; do kill -9 $pid; done
ps faux | grep gamescopereaper | grep -v grep | awk '{print $2}' | while read -r pid; do kill -9 $pid; done
