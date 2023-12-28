from src import com

if __name__ == "__main__":
    data = [] # 3D array [0][rows][phaseDiff(0)-magDiff(1)]
    for i in range(2):
        com.serial_collector(data_arr=data)
    print(data)