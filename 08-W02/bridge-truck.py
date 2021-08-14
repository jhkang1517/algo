def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = list()
    bridge_time = list()
    destination = list()
    destination_len = len(truck_weights)

    while True:

        if bridge_time != list():

            if bridge_time[0] + bridge_length == time:
                destination.append(bridge.pop(0))
                bridge_time.pop(0)

        if truck_weights != list():

            if truck_weights[0] + sum(bridge) > weight:
                pass

            else:
                bridge.append(truck_weights.pop(0))
                bridge_time.append(time)

        time += 1

        if destination_len == len(destination):
            break

    return time

