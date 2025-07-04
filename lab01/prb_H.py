import sys
input = sys.stdin.readline

def trains(ln, tr_l, ti_l, des):
    for i in range(1, ln):
        train = tr_l[i]; time = ti_l[i]; desti = des[i]
        j = i-1
        while j>=0 and (train<tr_l[j] or (train==tr_l[j] and time>ti_l[j])):           
            tr_l[j+1] = tr_l[j]; ti_l[j+1] = ti_l[j]; des[j+1] = des[j]
            j -= 1

        tr_l[j+1] = train; ti_l[j+1] = time; des[j+1] = desti

    for i in range(ln):
        print(f'{tr_l[i]} will departure for {des[i]} at {ti_l[i]}')


schedules = int(input())
train_list = []
time_list = []
des = []
for i in range(schedules):
    stat = input().split()    # must give .split() not .split(' ')
    train_list.append(stat[0])
    time_list.append(stat[len(stat)-1])
    des.append(stat[len(stat)-3])

trains(schedules, train_list, time_list, des)

