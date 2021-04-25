import psutil
import platform
from datetime import datetime
import json


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


########################### System information ###############################

def get_system_info():
    return {
        'System': platform.uname().system,
        'platform details': platform.platform(),
        'processor name': platform.processor(),
        'architectural detail': platform.architecture(),
        'hostname': platform.uname().node,
        'version': platform.uname().version 
    }

########################### Boot time ###############################

def get_boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return {
        'Boot Time': f'{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}'
    }

########################### CPU information ###############################

def get_cpu_info():
    cpufreq = psutil.cpu_freq()
    return {
        'Physical cores': psutil.cpu_count(logical=False),
        'Total cores': psutil.cpu_count(logical=True),
        'Max Frequency': f'{cpufreq.max:.2f}Mhz',
        'Min Frequency': f'{cpufreq.min:.2f}Mhz',
        'Current Frequency': f'{cpufreq.current:.2f}Mhz',
        'CPU Usage Per Core': get_cpu_usage(),
        'Total CPU Usage': f'{psutil.cpu_percent()}%'
    }

def get_cpu_usage():
    cpu_usage = {}
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        label = f'Core {i}'
        cpu_usage[label] = f'{percentage}%'
    
    return cpu_usage

########################### Memory information ###############################

def get_memory_info():
    svmem = psutil.virtual_memory()
    return {
        'Total': get_size(svmem.total),
        'Available': get_size(svmem.available),
        'Used': get_size(svmem.used),
        'Percentage': f'{svmem.percent}%'
    }

########################### Swap information ###############################

def get_swap_info():
    swap = psutil.swap_memory()
    return {
        'Total': get_size(swap.total),
        'Free': get_size(swap.free),
        'Used': get_size(swap.used),
        'Percentage': f'{swap.percent}%'
    }

########################### Disk information ###############################

def get_disk_info():
    disk_info = {}
    
    disk_io = psutil.disk_io_counters()
    partitions = psutil.disk_partitions()
    
    partitions_info = []
    for partition in partitions:
        temp = {
            'Device': partition.device,
            'Mountpoint': partition.mountpoint,
            'File system type': partition.fstype
        }
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        
        temp['Total Size'] = get_size(partition_usage.total)
        temp['Used'] = get_size(partition_usage.used)
        temp['Free'] = get_size(partition_usage.free)
        temp['Percentage'] = f'{partition_usage.percent}%'

        partitions_info.append(temp)


    return {
        'Partitions and Usage': partitions_info,
        'Total read': get_size(disk_io.read_bytes),
        'Total write': get_size(disk_io.write_bytes)
    }

########################### Network information ###############################

def get_network_info():
    interfaces = []
    if_addrs = psutil.net_if_addrs()
    net_io = psutil.net_io_counters()

    for interface_name, interface_addresses in if_addrs.items():
        interface = {}
        interface['Interface'] = interface_name
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                interface['IP Address'] = address.address
                interface['Netmask'] = address.netmask
                interface['Broadcast IP'] = address.broadcast
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                interface['MAC Address'] = address.address
                interface['MAC Netmask'] = address.netmask
                interface['Broadcast MAC'] = address.broadcast
    
        interfaces.append(interface)

    return {
        'Interfaces': interfaces,
        'Total Bytes Sent': get_size(net_io.bytes_sent),
        'Total Bytes Received': get_size(net_io.bytes_recv)
    }

############################ Haredware Information (all) ##############################

def get_hardware_info():
    return {
        'System Information': get_system_info(),
        'Boot Time': get_boot_time(),
        'CPU Information': get_cpu_info(),
        'Memory Information': get_memory_info(),
        'Swap Information': get_swap_info(),
        'Disk Information': get_disk_info(),
        'Network Information': get_network_info()
    }

if __name__ == "__main__":
    network_info = get_network_info()
    interfaces = network_info['Interfaces']

    for interface in interfaces:
        print('=================================')
        print(interface['Interface'])
    
    #print(json.dumps(interface, indent = 4))
    