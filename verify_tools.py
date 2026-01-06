import sys
import os

# Add current directory to path so we can import tools
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tools.system import get_system_status
from tools.shell import execute_command
from tools.audio import manage_volume

print("=== Testing System Status ===")
print(get_system_status())

print("\n=== Testing Shell Command (dir) ===")
print(execute_command("dir"))

print("\n=== Testing Audio (Get Volume) ===")
print(manage_volume("get"))

print("\n=== Testing Audio (Set Volume - Small change) ===")
# We won't blast the volume, just set it to a safe middle ground or current
print(manage_volume("set", level=20))

print("\n=== Verification Complete ===")
