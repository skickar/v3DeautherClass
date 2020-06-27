#!/bin/bash
esptool.py --port /dev/cu.wchusbserial14130 erase_flash
wait
esptool.py --port /dev/cu.wchusbserial14130 --baud 460800 write_flash --flash_size=detect 0 /Users/skickar/Desktop/esp_duck.ino.dstike.bin
wait
echo "All done, next"
sleep 5
screen /dev/cu.wchusbserial14130 115200
