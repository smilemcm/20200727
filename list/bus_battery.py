import sys

sys.stdin = open("bus_battery.txt","rt")
T = int(input())

for t in range(T):
    k, n, m = map(int, input().split())
    battery_charger_list = list(map(int, input().split()))

    bus_stations = [0] * (n+1)
    battery = k
    battery_refill_cnt = 0

    #### 모든 정거장에 충전소가 있던 없던 일단 0으로 세팅
    for i in range(len(bus_stations) ):
        for j in range(len(battery_charger_list)):
            ###정거장에 충전소가 있으면 1로 세팅
            if i == battery_charger_list[j]:
                bus_stations[i] = 1


    ### 여기서 부터는 실제 시뮬레이션
    for i in range(len(bus_stations)):
        battery = battery - 1


        ## 경우할 정류소에 배터리 충전소가 있을경우
        if sum(bus_stations[i:i+battery])>0:
            pass
        ### 이 버스 종류장에 충전소가 있으면 충전
        elif bus_stations[i] == 1:
            battery = k
            battery_refill_cnt = battery_refill_cnt + 1

        if battery == 0 and bus_stations[i] == 0:
            print("목적지에 도착하지 못했습니다.")
            battery_refill_cnt = 0
            break

    #print(t)
    print(t, battery_refill_cnt)



