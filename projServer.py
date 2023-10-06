import threading
import socket
import pygame
import struct
import random
import time
from flask import Flask, json, request, jsonify
# NEED_CREATE=True
LOGIN_PORT = 8884
MAIN_SEND_PORT = 8880
MAIN_RECV_PORT = 8883
SUB_SEND_PORT = 8881
SUB_RECV_PORT = 8882
backlog = 16
BUFSIZE = 1024
is_processing = False
ALL_CLIENT_LIST = [[], [], [], []]  # 開桌的
ALL_ALL_CLIENT_LIST = []  # 只是連線的[] 在線玩家
MEMBER_FILE = 'ID.json'
MEMBER = []  # 用MEMBER_FILE讀下來的大表格
condition_event = threading.Condition()
# ALL_CLIENT_LIST[main_send,main_recv,sub_send,sub_recv]
WAIT_TIME=0.02

def login_thread(client):
    while True:
        try:
            client_name = client.recv(BUFSIZE).decode('utf-8')
            username_Duplicate = 0  # 0代表沒有重複 1代表重複
            zero = 0
            temp = 0
            id = []
            password = []
            while(zero < len(client_name) and not(client_name[zero] == "&")):
                zero = zero + 1
            id = client_name[:zero]
            zero = zero + 1
            temp = zero
            while(zero < len(client_name) and not(client_name[zero] == "&")):
                zero = zero + 1
            password = client_name[temp:zero]
            check = 0
            print(id)
            print(password)
            if client_name[-1] == "0":
                # 登入
                # 確認帳號密碼
                while check < len(MEMBER):
                    if id == MEMBER[check]["USER_ID"]:
                        break
                    check = check + 1
                if check < len(MEMBER):
                    if password == MEMBER[check]["password"]:
                        pass  # 帳號密碼正確
                    else:
                        client.send(str(2).encode('utf-8'))
                        print(2)
                        continue
                        # return 2  # 密碼錯誤
                else:
                    client.send(str(1).encode('utf-8'))
                    print(1)
                    continue
                    # return 1  # 帳號不存在

                # 判斷名稱是否一樣 不能重複登入
                found = 0
                i = 0
                while i < len(ALL_ALL_CLIENT_LIST):
                    if ALL_ALL_CLIENT_LIST[i][1] == client_name:
                        print("SAME NAME")
                        found = 1
                        break
                    i += 1
                if found == 0:
                    ALL_ALL_CLIENT_LIST.append([client, client_name])
                    client.send(str(3).encode('utf-8'))
                    print(3)
                    continue
                    # return 3  # 登入成功
                elif found == 1:
                    client.send(str(4).encode('utf-8'))
                    print(4)
                    continue
                    # return 4  # 重複登入

            if client_name[-1] == "1":
                for i in range(len(MEMBER)):
                    if id == MEMBER[i]["USER_ID"]:
                        client.send(str(-1).encode('utf-8'))
                        print(-1)
                        username_Duplicate = 1
                        # return -1
                if username_Duplicate == 0:
                    MEMBER.append({"USER_ID": id, "password": password})
                    with open(MEMBER_FILE, 'w') as wfp:
                        json.dump(MEMBER, wfp)
                    client.send(str(1).encode('utf-8'))
                    print(11)
            username_Duplicate = 0
        except:
            for i in range(len(ALL_ALL_CLIENT_LIST)):
                if ALL_ALL_CLIENT_LIST[i][1] == client_name:
                    del ALL_ALL_CLIENT_LIST[i]
                    break
            break


def login_area():
    global ALL_ALL_CLIENT_LIST
    login_srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    login_srvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    login_srvSocket.bind(('127.0.0.1', LOGIN_PORT))
    login_srvSocket.listen(backlog)
    global MEMBER

    while True:
        client, (rip, rport) = login_srvSocket.accept()
        thread_send = threading.Thread(target=login_thread, args=(client,))
        thread_send.setDaemon(True)
        thread_send.start()


def wait_main_send_client():
    global ALL_CLIENT_LIST
    global is_processing
    main_send_srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_send_srvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    main_send_srvSocket.bind(('127.0.0.1', MAIN_SEND_PORT))
    main_send_srvSocket.listen(backlog)

    while True:
        is_processing = False
        wait_people_num=-1
        client = ""
        client, (rip, rport) = main_send_srvSocket.accept()
        client_name = client.recv(BUFSIZE).decode('utf-8')
        #print("main wait")
        while is_processing:
            pass
        is_processing = True
        #print("main", client_name)
        found = 0
        full = 0
        i = 0
        while i < len(ALL_CLIENT_LIST):
            j = 0
            while j < len(ALL_CLIENT_LIST[i]) and j<4:
                if ALL_CLIENT_LIST[i][j][4] == client_name:
                    found = 1
                    if ALL_CLIENT_LIST[i][j][0] != 0:
                        full = 1
                    break
                j += 1
            if found == 1:
                break
            i += 1
        if found == 0:
            #print("main no found")
            i = 0
            while len(ALL_CLIENT_LIST[i]) >= 4:
                i += 1
                if i == 4:
                    full = 1
                    break
            if full == 0:
                wait_people_num = 3 - len(ALL_CLIENT_LIST[i])
                ALL_CLIENT_LIST[i].append([client, 0, 0, 0, client_name])
                print(f"to {i}-{len(ALL_CLIENT_LIST[i])-1}")
                #print("main new ", i, " ", len(ALL_CLIENT_LIST[i])-1)
            if full == 1:
                pass
                # time_event.clear()
                # time_event.wait()
        elif found == 1 and full == 0:
            wait_people_num = 3 - len(ALL_CLIENT_LIST[i])
            ALL_CLIENT_LIST[i][j][0] = client
            #print("main add ", i, " ", j)

        time.sleep(WAIT_TIME)
        print("wait_people start")
        j=0
        while j<len(ALL_CLIENT_LIST[i]):
            try:
                ALL_CLIENT_LIST[i][j][0].send("2".encode('utf-8'))
                time.sleep(WAIT_TIME)
                ALL_CLIENT_LIST[i][j][0].send("wait_people".encode('utf-8'))
                time.sleep(WAIT_TIME)
                ALL_CLIENT_LIST[i][j][0].send(str(wait_people_num).encode('utf-8'))
                time.sleep(WAIT_TIME)
            except:
                pass
            j+=1
        print("wait_people end")
        i = 0
        while i < len(ALL_CLIENT_LIST):
            ready = 1
            if len(ALL_CLIENT_LIST[i]) == 4:
                #print("main ready")
                j = 0
                while j < 4:
                    if ALL_CLIENT_LIST[i][j][0] == 0 or ALL_CLIENT_LIST[i][j][1] == 0 or ALL_CLIENT_LIST[i][j][2] == 0 or ALL_CLIENT_LIST[i][j][3] == 0:
                        ready = 0
                        # print("main not ready",ALL_CLIENT_LIST[i][j][0]==0 , ALL_CLIENT_LIST[i][j][1]==0 , ALL_CLIENT_LIST[i][j][2]==0)
                    j += 1

                if ready == 1:
                    play_t = threading.Thread(
                        target=play, args=(ALL_CLIENT_LIST[i],))
                    play_t.setDaemon(True)
                    play_t.start()
                    ALL_CLIENT_LIST[i].append(i)

            i += 1


def wait_main_recv_client():
    global ALL_CLIENT_LIST
    global is_processing
    main_recv_srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_recv_srvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    main_recv_srvSocket.bind(('127.0.0.1', MAIN_RECV_PORT))
    main_recv_srvSocket.listen(backlog)

    while True:
        is_processing = False
        client = ""
        client, (rip, rport) = main_recv_srvSocket.accept()
        client_name = client.recv(BUFSIZE).decode('utf-8')
        #print("main wait")
        while is_processing:
            pass
        is_processing = True
        #print("main", client_name)
        found = 0
        full = 0
        i = 0
        while i < len(ALL_CLIENT_LIST):
            j = 0
            while j < len(ALL_CLIENT_LIST[i]) and j<4:
                if ALL_CLIENT_LIST[i][j][4] == client_name:
                    found = 1
                    if ALL_CLIENT_LIST[i][j][1] != 0:
                        full = 1
                    break
                j += 1
            if found == 1:
                break
            i += 1
        if found == 0:
            #print("main no found")
            i = 0
            while len(ALL_CLIENT_LIST[i]) >= 4:
                i += 1
                if i == 4:
                    full = 1
                    break
            if full == 0:
                ALL_CLIENT_LIST[i].append([0, client, 0, 0, client_name])
                print(f"to {i}-{len(ALL_CLIENT_LIST[i])-1}")
                #print("main new ", i, " ", len(ALL_CLIENT_LIST[i])-1)
            if full == 1:
                pass
                # time_event.clear()
                # time_event.wait()
        elif found == 1 and full == 0:
            ALL_CLIENT_LIST[i][j][1] = client
            #print("main add ", i, " ", j)

        i = 0
        while i < len(ALL_CLIENT_LIST):
            ready = 1
            if len(ALL_CLIENT_LIST[i]) == 4:
                #print("main ready")
                j = 0
                while j < 4:
                    if ALL_CLIENT_LIST[i][j][0] == 0 or ALL_CLIENT_LIST[i][j][1] == 0 or ALL_CLIENT_LIST[i][j][2] == 0 or ALL_CLIENT_LIST[i][j][3] == 0:
                        ready = 0
                        # print("main not ready",ALL_CLIENT_LIST[i][j][0]==0 , ALL_CLIENT_LIST[i][j][1]==0 , ALL_CLIENT_LIST[i][j][2]==0)
                    j += 1

                if ready == 1:
                    play_t = threading.Thread(
                        target=play, args=(ALL_CLIENT_LIST[i],))
                    play_t.setDaemon(True)
                    play_t.start()
                    ALL_CLIENT_LIST[i].append(i)

            i += 1


def wait_sub_send_client():
    global ALL_CLIENT_LIST
    global is_processing
    sub_send_srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sub_send_srvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sub_send_srvSocket.bind(('127.0.0.1', SUB_SEND_PORT))
    sub_send_srvSocket.listen(backlog)

    while True:
        is_processing = False
        client = ""
        client, (rip, rport) = sub_send_srvSocket.accept()
        client_name = client.recv(BUFSIZE).decode('utf-8')
        #print("sub send wait")
        while is_processing:
            pass
        is_processing = True
        #print("sub send ", client_name)
        found = 0
        full = 0
        i = 0
        while i < len(ALL_CLIENT_LIST):
            j = 0
            while j < len(ALL_CLIENT_LIST[i])and j<4:
                if ALL_CLIENT_LIST[i][j][4] == client_name:
                    found = 1
                    if ALL_CLIENT_LIST[i][j][2] != 0:
                        full = 1
                    break
                j += 1
            if found == 1:
                break
            i += 1
        if found == 0:
            #print("sub no found")
            i = 0
            while len(ALL_CLIENT_LIST[i]) >= 4:
                i += 1
                if i == 4:
                    full = 1
                    break
            if full == 0:
                ALL_CLIENT_LIST[i].append([0, 0, client, 0, client_name])
                print(f"to {i}-{len(ALL_CLIENT_LIST[i])-1}")
                #print("sub send new ", i, " ", len(ALL_CLIENT_LIST[i])-1)
            if full == 1:
                pass
                # time_event.clear()
                # time_event.wait()
        elif found == 1 and full == 0:
            ALL_CLIENT_LIST[i][j][2] = client
            #print("sub send add ", i, " ", j)

        i = 0
        while i < len(ALL_CLIENT_LIST):
            ready = 1
            #print(len(ALL_CLIENT_LIST[i]))
            if len(ALL_CLIENT_LIST[i]) == 4:
                #print("sub send ready")
                j = 0
                while j < 4:
                    if ALL_CLIENT_LIST[i][j][0] == 0 or ALL_CLIENT_LIST[i][j][1] == 0 or ALL_CLIENT_LIST[i][j][2] == 0 or ALL_CLIENT_LIST[i][j][3] == 0:
                        ready = 0
                        # print("sub send not ready",ALL_CLIENT_LIST[i][j][0]==0 , ALL_CLIENT_LIST[i][j][1]==0 , ALL_CLIENT_LIST[i][j][2]==0)
                    j += 1

                if ready == 1:
                    play_t = threading.Thread(
                        target=play, args=(ALL_CLIENT_LIST[i],))
                    play_t.setDaemon(True)
                    play_t.start()
                    ALL_CLIENT_LIST[i].append(i)

            i += 1


def wait_sub_recv_client():
    global ALL_CLIENT_LIST
    global is_processing
    sub_recv_srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sub_recv_srvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sub_recv_srvSocket.bind(('127.0.0.1', SUB_RECV_PORT))
    sub_recv_srvSocket.listen(backlog)

    while True:
        is_processing = False
        client = ""
        client, (rip, rport) = sub_recv_srvSocket.accept()
        client_name = client.recv(BUFSIZE).decode('utf-8')
        #print("sub recv wait")
        while is_processing:
            pass
        is_processing = True
        #print("sub recv", client_name)
        found = 0
        full = 0
        i = 0
        while i < len(ALL_CLIENT_LIST):
            j = 0
            while j < len(ALL_CLIENT_LIST[i])and j<4:
                if ALL_CLIENT_LIST[i][j][4] == client_name:
                    found = 1
                    if ALL_CLIENT_LIST[i][j][3] != 0:
                        full = 1
                    break
                j += 1
            if found == 1:
                break
            i += 1
        if found == 0:
            #print("sub recv no found")
            i = 0
            while len(ALL_CLIENT_LIST[i]) >= 4:
                i += 1
                if i == 4:
                    full = 1
                    break
            if full == 0:
                ALL_CLIENT_LIST[i].append([0, 0, 0, client, client_name])
                print(f"to {i}-{len(ALL_CLIENT_LIST[i])-1}")
                #print("sub recv new ", i, " ", len(ALL_CLIENT_LIST[i])-1)
            if full == 1:
                pass
                # time_event.clear()
                # time_event.wait()
                #print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        elif found == 1 and full == 0:
            ALL_CLIENT_LIST[i][j][3] = client
            #print("sub recv add ", i, " ", j)
        else:
            pass
            #print("sub recv found:", found, "full:", full)

        i = 0
        while i < len(ALL_CLIENT_LIST):
            ready = 1
            #print(len(ALL_CLIENT_LIST[i]))
            if len(ALL_CLIENT_LIST[i]) == 4:
                #print("sub recv ready")
                j = 0
                while j < 4:
                    if ALL_CLIENT_LIST[i][j][0] == 0 or ALL_CLIENT_LIST[i][j][1] == 0 or ALL_CLIENT_LIST[i][j][2] == 0 or ALL_CLIENT_LIST[i][j][3] == 0:
                        ready = 0
                        # print("sub recv  not ready",ALL_CLIENT_LIST[i][j][0]==0 , ALL_CLIENT_LIST[i][j][1]==0 , ALL_CLIENT_LIST[i][j][2]==0)
                    j += 1

                if ready == 1:
                    play_t = threading.Thread(
                        target=play, args=(ALL_CLIENT_LIST[i],))
                    play_t.setDaemon(True)
                    play_t.start()
                    ALL_CLIENT_LIST[i].append(i)

            i += 1


def end_socket_processing(clear_name_list):
    global ALL_CLIENT_LIST
    isbreak = 0
    k = 0
    while k < len(clear_name_list):
        i = 0
        while i < len(ALL_CLIENT_LIST):
            j = 0
            while j < len(ALL_CLIENT_LIST[i]):
                if ALL_CLIENT_LIST[i][j][4] == clear_name_list[k]:
                    condition_event.acquire()
                    l = 0
                    while l < 4:
                        ALL_CLIENT_LIST[i][l][0].close()
                        ALL_CLIENT_LIST[i][l][1].close()
                        ALL_CLIENT_LIST[i][l][2].close()
                        ALL_CLIENT_LIST[i][l][3].close()
                        l += 1
                    ALL_CLIENT_LIST[i] = []
                    condition_event.release()
                    isbreak = 1
                    break
                j += 1
            if isbreak == 1:
                break
            i += 1
        if isbreak == 1:
            break
        k += 1




def countdown_send(GV, send_c, second=20):

    print("start countdown")
    i = second
    GV.time_event.clear()
    while i >= 0 and not GV.time_event.is_set() and GV.TIME_EVENT_SET != 1:
        try:
            send_c.send(str(i).encode('utf-8'))
        except:
            GV.LEAVE = 1
            break
        print(i)
        GV.time_event.wait(1)
        i -= 1
    if i < 0 or GV.time_event.is_set():
        GV.IS_COUNTDOWN_FINISH = 1
    else:
        GV.IS_COUNTDOWN_FINISH = 0

    print("countdown_send finish")


def countdown_recv(GV, recv_c, target_name):
    while True:
        try:
            c_name = recv_c.recv(BUFSIZE).decode('utf-8')
        except:
            GV.LEAVE = 1
            break
        if c_name == target_name:
            GV.time_event.set()


def single_data_recv(GV, send_c_list, recv_c, id):
    data = ""
    while True:
        try:
            data = recv_c.recv(BUFSIZE).decode('utf-8')
        except:
            GV.LEAVE = 1
            break
        if GV.SEND_FINISH == 1:
            break
        if data.isdigit():
            GV.DATA_LIST[id] = []
            i = 0
            while i < int(data):
                try:
                    data2 = recv_c.recv(BUFSIZE).decode('utf-8')
                    GV.DATA_LIST[id].append(data2)
                except:
                    GV.LEAVE = 1
                    break
                i += 1
            print(GV.DATA_LIST[id])
            if GV.DATA_LIST[id][0] == "leave":  # 某家中斷連線
                i = 0
                while i < 4:
                    if i != id:
                        try:
                            send_c_list[i].send("1".encode('utf-8'))
                            send_c_list[i].send("leave".encode('utf-8'))
                        except:
                            pass
                    i += 1
                GV.LEAVE = 1
                break
            elif GV.DATA_LIST[id][0] == "end":  # 某家遊戲結束
                pass
            elif GV.DATA_LIST[id][0] == "out":  # 收到牌
                #with GV.condition_event:
                #    GV.condition_event.acquire()
                GV.SEND_DATA[id] = GV.DATA_LIST[id][1]
                print("id: ", id, " recved: ", GV.SEND_DATA[id])
                i=0
                while i<len(GV.player_list[id].card_list):
                    if GV.player_list[id].card_list[i] == GV.SEND_DATA[id]:
                        del GV.player_list[id].card_list[i]
                        break
                    i+=1
                # while not GV.IS_WAITING_DATA:
                #	pass
                # print("while break")
                GV.TIME_EVENT_SET = 1
                print("TIME_EVENT_SET=1,out")
            elif GV.DATA_LIST[id][0] == "chi":  # 吃
                i = 0
                id1 = 1
                id2 = 1
                while i < len(GV.player_list[id].card_list) and (id1 == 1 or id2 == 1):
                    if GV.player_list[id].card_list[i] == GV.DATA_LIST[id][1] and id1 == 1:
                        id1 = 0
                        del GV.player_list[id].card_list[i]
                    elif GV.player_list[id].card_list[i] == GV.DATA_LIST[id][2] and id2 == 1:
                        id2 = 0
                        del GV.player_list[id].card_list[i]
                    i += 1
                GV.player_list[id].vice_dews.append(
                    [GV.DATA_LIST[id][1], GV.DATA_LIST[id][2], GV.DATA_LIST[id][3]])
                GV.IS_CHI = 1
                GV.TIME_EVENT_SET = 1
                print("TIME_EVENT_SET=1,chi")
            elif GV.DATA_LIST[id][0] == "pong":  # 碰
                delnum = 0
                while i < len(GV.player_list[id].card_list) and delnum < 2:
                    if GV.player_list[id].card_list[i] == GV.DATA_LIST[id][1]:
                        delnum += 1
                        del GV.player_list[id].card_list[i]
                    i += 1

                GV.player_list[id].vice_dews.append(
                    [GV.DATA_LIST[id][1], GV.DATA_LIST[id][1], GV.DATA_LIST[id][1]])
                GV.IS_PONG = 1
                GV.TIME_EVENT_SET = 1
                print("TIME_EVENT_SET=1,pong")
            elif GV.DATA_LIST[id][0] == "kong":  # 槓
                delnum = 0
                while i < len(GV.player_list[id].card_list) and delnum < 3:
                    if GV.player_list[id].card_list[i] == GV.DATA_LIST[id][1]:
                        delnum += 1
                        del GV.player_list[id].card_list[i]
                    i += 1

                GV.player_list[id].vice_dews.append(
                    [GV.DATA_LIST[id][1], GV.DATA_LIST[id][1], GV.DATA_LIST[id][1], GV.DATA_LIST[id][1]])

                GV.IS_KONG = 1
                GV.TIME_EVENT_SET = 1
                print("TIME_EVENT_SET=1,kong")
            elif GV.DATA_LIST[id][0] == "tsumo":  # 自摸

                GV.IS_WIN = 1
                GV.TIME_EVENT_SET = 1
                print("TIME_EVENT_SET=1,tsumo")
            elif GV.DATA_LIST[id][0] == "ron":  # ron
                GV.IS_WIN = 1
                GV.TIME_EVENT_SET = 1
                print("TIME_EVENT_SET=1,ron")
            elif GV.DATA_LIST[id][0] == "cancel":
                GV.IS_CHI = 0
                GV.IS_PONG = 0
                GV.IS_KONG = 0
                GV.TIME_EVENT_SET = 1
                print("TIME_EVENT_SET=1,cancel")
            

################################################################################################################


def shuffle(GV):  # 洗牌, 之後要丟到server
    # global REMAINING_MAHJONG_LIST
    # global CARD_MOUNTAIN
    GV.REMAINING_MAHJONG_LIST = ["Man1", "Man1", "Man1", "Man1", "Man2", "Man2", "Man2", "Man2", "Man3", "Man3", "Man3", "Man3", "Man4", "Man4", "Man4", "Man4", "Man5", "Man5", "Man5", "Man6", "Man6", "Man6", "Man6", "Man7", "Man7", "Man7", "Man7", "Man8", "Man8", "Man8", "Man8", "Man9", "Man9", "Man9", "Man9", "Pin1", "Pin1", "Pin1", "Pin1", "Pin2", "Pin2", "Pin2", "Pin2", "Pin3", "Pin3", "Pin3", "Pin3", "Pin4", "Pin4", "Pin4", "Pin4", "Pin5", "Pin5", "Pin5", "Pin6", "Pin6", "Pin6", "Pin6", "Pin7", "Pin7", "Pin7", "Pin7", "Pin8", "Pin8", "Pin8", "Pin8", "Pin9",
                                 "Pin9", "Pin9", "Pin9", "Sou1", "Sou1", "Sou1", "Sou1", "Sou2", "Sou2", "Sou2", "Sou2", "Sou3", "Sou3", "Sou3", "Sou3", "Sou4", "Sou4", "Sou4", "Sou4", "Sou5", "Sou5", "Sou5", "Sou6", "Sou6", "Sou6", "Sou6", "Sou7", "Sou7", "Sou7", "Sou7", "Sou8", "Sou8", "Sou8", "Sou8", "Sou9", "Sou9", "Sou9", "Sou9", "Ton", "Ton", "Ton", "Ton", "Nan", "Nan", "Nan", "Nan", "Shaa", "Shaa", "Shaa", "Shaa", "Pei", "Pei", "Pei", "Pei", "Chun", "Chun", "Chun", "Chun", "Haku", "Haku", "Haku", "Haku", "Hatsu", "Hatsu", "Hatsu", "Hatsu", "Man5_red", "Pin5_red", "Sou5_red"]

    while len(GV.REMAINING_MAHJONG_LIST) > 0:
        rand_index = random.randint(0, len(GV.REMAINING_MAHJONG_LIST)-1)
        GV.CARD_MOUNTAIN.append(GV.REMAINING_MAHJONG_LIST[rand_index])
        del GV.REMAINING_MAHJONG_LIST[rand_index]


def start_deal(GV, player_list):
    if GV.MANAGE_MODE == 0:
        seed = GV.SEED
        i = 0
        while i < 52:
            if i < 48:
                if seed == 1:
                    for one in range(4):
                        deal(GV, player_list[0])
                elif seed == 2:
                    for one in range(4):
                        deal(GV, player_list[1])
                elif seed == 3:
                    for one in range(4):
                        deal(GV, player_list[2])
                elif seed == 4:
                    for one in range(4):
                        deal(GV, player_list[3])
                i += 4
            else:
                if seed == 1:
                    deal(GV, player_list[0])
                elif seed == 2:
                    deal(GV, player_list[1])
                elif seed == 3:
                    deal(GV, player_list[2])
                elif seed == 4:
                    deal(GV, player_list[3])
                i += 1
            seed += 1
            if seed > 4:
                seed = 1
        seed -= 1
        if seed <= 0:
            seed = 4
        return GV.SEED
    else:  # (自訂手牌)
        i = 0
        while i < 4:
            player_list[i].card_list = GV.self_define_cards[i]
            # print(player_list[i].card_list)
            print("PLAYER:", i)
            j = 0
            while j < len(player_list[i].card_list):
                k = 0
                while k < len(GV.CARD_MOUNTAIN):
                    if player_list[i].card_list[j] == GV.CARD_MOUNTAIN[k]:
                        # print("刪了啦幹")
                        del GV.CARD_MOUNTAIN[k]
                        print("GV LEN:", len(GV.CARD_MOUNTAIN))
                        break
                    k += 1
                j += 1
            i += 1
        return GV.SEED


def deal(GV, Player, type=""):  # 發牌, type="","draw"

    if type == "draw":
        Player.deal_card = GV.CARD_MOUNTAIN[0]
    else:
        Player.card_list.append(GV.CARD_MOUNTAIN[0])

    del GV.CARD_MOUNTAIN[0]


MAHJONG_SORT_TABLE_LIST = ["Man1", "Man2", "Man3", "Man4", "Man5", "Man5_red", "Man6", "Man7", "Man8", "Man9", "Pin1", "Pin2", "Pin3", "Pin4", "Pin5", "Pin5_red", "Pin6",
                                                   "Pin7", "Pin8", "Pin9", "Sou1", "Sou2", "Sou3", "Sou4", "Sou5", "Sou5_red", "Sou6", "Sou7", "Sou8", "Sou9", "Ton", "Nan", "Shaa", "Pei", "Chun", "Haku", "Hatsu"]


def sort(player_list):  # 排牌
    i = 0
    while i < 4:
        list = []
        for j in range(len(player_list[i].card_list)):
            list.append(MAHJONG_SORT_TABLE_LIST.index(
                player_list[i].card_list[j]))
        j = 0
        while j < len(list):
            k = j+1
            while k < len(list):
                if list[j] > list[k]:
                    list[j], list[k] = list[k], list[j]
                    player_list[i].card_list[j], player_list[i].card_list[k] = player_list[i].card_list[k], player_list[i].card_list[j]
                k += 1

            j += 1
        i += 1


NEXT_SITE_INDEX = {"down": 1, "right": 2, "up": 3, "left": 0}
SITE_INDEX = {"down": 0, "right": 1, "up": 2, "left": 3}

CHI_TABLE = {
    "Man1": [["Man2", "Man3"]],
    "Man2": [["Man1", "Man3"], ["Man3", "Man4"]],
    "Man3": [["Man1", "Man2"], ["Man2", "Man4"], ["Man4", "Man5"], ["Man4", "Man5_red"]],
    "Man4": [["Man2", "Man3"], ["Man3", "Man5"], ["Man3", "Man5_red"], ["Man5", "Man6"], ["Man5_red", "Man6"]],
    "Man5": [["Man3", "Man4"], ["Man4", "Man6"], ["Man6", "Man7"]],
    "Man5_red": [["Man3", "Man4"], ["Man4", "Man6"], ["Man6", "Man7"]],
    "Man6": [["Man4", "Man5"], ["Man4", "Man5_red"], ["Man5", "Man7"], ["Man5_red", "Man7"], ["Man7", "Man8"]],
    "Man7": [["Man5", "Man6"], ["Man5_red", "Man6"], ["Man6", "Man8"], ["Man8", "Man9"]],
    "Man8": [["Man6", "Man7"], ["Man7", "Man9"]],
    "Man9": [["Man7", "Man8"]],
    "Pin1": [["Pin2", "Pin3"]],
    "Pin2": [["Pin1", "Pin3"], ["Pin3", "Pin4"]],
    "Pin3": [["Pin1", "Pin2"], ["Pin2", "Pin4"], ["Pin4", "Pin5"], ["Pin4", "Pin5_red"]],
    "Pin4": [["Pin2", "Pin3"], ["Pin3", "Pin5"], ["Pin3", "Pin5_red"], ["Pin5", "Pin6"], ["Pin5_red", "Pin6"]],
    "Pin5": [["Pin3", "Pin4"], ["Pin4", "Pin6"], ["Pin6", "Pin7"]],
    "Pin5_red": [["Pin3", "Pin4"], ["Pin4", "Pin6"], ["Pin6", "Pin7"]],
    "Pin6": [["Pin4", "Pin5"], ["Pin4", "Pin5_red"], ["Pin5", "Pin7"], ["Pin5_red", "Pin7"], ["Pin7", "Pin8"]],
    "Pin7": [["Pin5", "Pin6"], ["Pin5_red", "Pin6"], ["Pin6", "Pin8"], ["Pin8", "Pin9"]],
    "Pin8": [["Pin6", "Pin7"], ["Pin7", "Pin9"]],
    "Pin9": [["Pin7", "Pin8"]],
    "Sou1": [["Sou2", "Sou3"]],
    "Sou2": [["Sou1", "Sou3"], ["Sou3", "Sou4"]],
    "Sou3": [["Sou1", "Sou2"], ["Sou2", "Sou4"], ["Sou4", "Sou5"], ["Sou4", "Sou5_red"]],
    "Sou4": [["Sou2", "Sou3"], ["Sou3", "Sou5"], ["Sou3", "Sou5_red"], ["Sou5", "Sou6"], ["Sou5_red", "Sou6"]],
    "Sou5": [["Sou3", "Sou4"], ["Sou4", "Sou6"], ["Sou6", "Sou7"]],
    "Sou5_red": [["Sou3", "Sou4"], ["Sou4", "Sou6"], ["Sou6", "Sou7"]],
    "Sou6": [["Sou4", "Sou5"], ["Sou4", "Sou5_red"], ["Sou5", "Sou7"], ["Sou5_red", "Sou7"], ["Sou7", "Sou8"]],
    "Sou7": [["Sou5", "Sou6"], ["Sou5_red", "Sou6"], ["Sou6", "Sou8"], ["Sou8", "Sou9"]],
    "Sou8": [["Sou6", "Sou7"], ["Sou7", "Sou9"]],
    "Sou9": [["Sou7", "Sou8"]],
}

def deal_with_card(GV,site,append_card_id):
    if site == "down":
        GV.player_list[0].card_list.append(append_card_id)
        GV.player_list[0].deal_card=""
    elif site == "right":
        GV.player_list[1].card_list.append(append_card_id)
        GV.player_list[1].deal_card=""
    elif site == "up":
        GV.player_list[2].card_list.append(append_card_id)
        GV.player_list[2].deal_card=""
    elif site == "left":
        GV.player_list[3].card_list.append(append_card_id)
        GV.player_list[3].deal_card=""
        
    

def other_can_chi(GV, player_list, site, mahjong_id):  # 判斷是否可以吃牌
    can_or_can_not = False
    print("player_list[NEXT_SITE_INDEX[site]].card_list",player_list[NEXT_SITE_INDEX[site]].card_list)
    try:
        possiable_combination_list = CHI_TABLE[mahjong_id]
    except:
        return [False, []]

    comb_card1_id = ""
    comb_card2_id = ""
    found_card1 = False
    found_card2 = False
    target_cards = []  # 存可組合的牌id

    GV.CAN_CHI[NEXT_SITE_INDEX[site]] = 0
    i = 0
    while i < len(possiable_combination_list):
        found_card1 = False
        found_card2 = False
        comb_card1_id = possiable_combination_list[i][0]
        comb_card2_id = possiable_combination_list[i][1]
        j = 0
        while j < len(player_list[NEXT_SITE_INDEX[site]].card_list):
            if comb_card1_id == player_list[NEXT_SITE_INDEX[site]].card_list[j]:
                found_card1 = True
                break
            j += 1
        while j < len(player_list[NEXT_SITE_INDEX[site]].card_list):
            if comb_card2_id == player_list[NEXT_SITE_INDEX[site]].card_list[j]:
                found_card2 = True
                break
            j += 1
        if found_card1 and found_card2:
            target_cards.append([comb_card1_id, comb_card2_id])
            GV.CAN_CHI[NEXT_SITE_INDEX[site]] = 1
            can_or_can_not = True
        i += 1

    i = 0
    while i < 4:
        if i != NEXT_SITE_INDEX[site]:
            GV.CAN_CHI[i] = 0
        i += 1

    return [can_or_can_not, target_cards]


def others_can_pong_or_kong(GV, player_list, site, mahjong_id):  # 判斷是否可以碰牌&槓牌
    mahjong_number = MAHJONG_SORT_TABLE_LIST.index(mahjong_id)
    # 進來是紅寶只需要找普通牌
    if mahjong_number == 5 or mahjong_number == 15 or mahjong_number == 25:
        mahjong_number = mahjong_number == 5 - 1
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "down":
        for i in range(len(player_list[0].card_list)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(player_list[0].card_list[i]))
        for i in range(len(player_list[0].card_list)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[0].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[0].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[0].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            GV.CAN_PONG[0] = 1
            return[True, "CAN_PONG", 0]
        elif len(index) == 3:
            GV.CAN_KONG[0] = 1
            GV.CAN_PONG[0] = 1
            return[True, "CAN_PONG_AND_KONG", 0]
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "right":
        for i in range(len(player_list[1].card_list)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(player_list[1].card_list[i]))
        for i in range(len(player_list[1].card_list)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[1].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[1].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[1].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            GV.CAN_PONG[1] = 1
            return[True, "CAN_PONG", 1]
        elif len(index) == 3:
            GV.CAN_KONG[1] = 1
            GV.CAN_PONG[1] = 1
            return[True, "CAN_PONG_AND_KONG", 1]
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "up":
        for i in range(len(player_list[2].card_list)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(player_list[2].card_list[i]))
        for i in range(len(player_list[2].card_list)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[2].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[2].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[2].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            GV.CAN_PONG[2] = 1
            return[True, "CAN_PONG", 2]
        elif len(index) == 3:
            GV.CAN_KONG[2] = 1
            GV.CAN_PONG[2] = 1
            return[True, "CAN_PONG_AND_KONG", 2]
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "left":
        for i in range(len(player_list[3].card_list)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(player_list[3].card_list[i]))
        for i in range(len(player_list[3].card_list)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[3].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[3].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(player_list[3].card_list)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            GV.CAN_PONG[3] = 1
            return[True, "CAN_PONG", 3]
        elif len(index) == 3:
            GV.CAN_KONG[3] = 1
            GV.CAN_PONG[3] = 1
            return[True, "CAN_PONG_AND_KONG", 3]
    return[False, "null", -1]


def can_win(GV, site, draw):  # 判斷是否可以和牌
    print("CANWINNNNNNNNNNNNNNNNNNNN")
    # 計算順序為
    # 1. 先把對子抓出來，並將1萬到白發中全都餵過一遍
    # 2. 一萬刻先抓，沒刻抓123萬 順 以此類推
    # 3. 若餵到能聽牌的結果，存入listen，並繼續
    # 4. 當一組餵完之後，從剛剛抓出對子的下一個next_pairs 繼續尋找對子出來抓 並重複23
    # 5. 當y 也就是對子找到最後一組時 break
    # 6. 把listen轉成id傳回去
    hand_card_number_list = []
    hand_card_number_list_copy = []
    next_pairs = 0  # 下一個對
    score_eyes = 0  # 有沒有一組眼
    xtriplet = 0  # 順的輪次
    offset = 0  # 同一輪次 刻順的位移 刻在順前面
    fourteen = 0  # 判斷手牌是否全 -1
    temp = []
    list = []
    score = 0
    while True:
        if site == "down":
            hand_card_number_list = []
            # GV.player_list[0].card_list
            for i in range(len(GV.player_list[0].card_list)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(GV.player_list[0].card_list[i]))
        if site == "right":
            hand_card_number_list = []
            for i in range(len(GV.player_list[1].card_list)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(GV.player_list[1].card_list[i]))
        if site == "up":
            hand_card_number_list = []
            for i in range(len(GV.player_list[2].card_list)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(GV.player_list[2].card_list[i]))
        if site == "left":
            hand_card_number_list = []
            for i in range(len(GV.player_list[3].card_list)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(GV.player_list[3].card_list[i]))
        hand_card_number_list.append(
            MAHJONG_SORT_TABLE_LIST.index(draw))
        hand_card_number_list.sort()

        xtriplet = 0  # 順的輪次
        offset = 0  # 同一輪次 刻順的位移 刻在順前面

        y_pair = next_pairs
        score_eyes = 0
        fourteen = 0
        hand_card_number_list_copy = hand_card_number_list
        temp = []
        list = []
        score = 0
        # 對子
        for xx in range(len(SEQUENCE)):
            # y_pair 確認內容是否符合
            while (y_pair in SEQUENCE[xx]):
                temp = [i for i, find in enumerate(
                        hand_card_number_list_copy) if find == y_pair]
                for z in range(len(temp)):
                    list.append(temp[z])
                y_pair = y_pair + 1
            if len(list) >= 2:
                hand_card_number_list_copy[list[0]] = -1
                hand_card_number_list_copy[list[1]] = -1
                score_eyes = score_eyes + 1
            if score_eyes >= 1:
                break
            else:
                # print("False")
                # return (False)
                pass
            list = []
        next_pairs = y_pair
        list = []
        # 刻子
        for x in range(len(SEQUENCE)):
            # y 確認內容是否符合
            for y1 in SEQUENCE[x]:
                temp = [i for i, find in enumerate(
                        hand_card_number_list_copy) if find == y1]

                for z in range(len(temp)):
                    list.append(temp[z])
            if len(list) == 3:
                hand_card_number_list_copy[list[0]] = -1
                hand_card_number_list_copy[list[1]] = -1
                hand_card_number_list_copy[list[2]] = -1
                score = score + 3
            elif len(list) == 4:
                hand_card_number_list_copy[list[0]] = -1
                hand_card_number_list_copy[list[1]] = -1
                hand_card_number_list_copy[list[3]] = -1
                score = score + 3
            else:
                pass
            list = []

            if xtriplet < 29:
                # 順子 跟刻子要同輪次
                if(x == 8 or x == 9 or x == 18 or x == 19 or x == 28 or x == 29):
                    offset = offset - 1
                else:
                    xtriplet = x + offset
                    # print(f"\n{xtriplet, x}\n")
                    # print("---" + str(xtriplet))
                    # y 確認內容是否符合
                    for z in range(3):
                        for y in range(len(TRIPLET[xtriplet])):
                            if TRIPLET[xtriplet][y] in hand_card_number_list_copy:
                                list.append(
                                    hand_card_number_list_copy.index(TRIPLET[xtriplet][y]))
                        if len(list) >= 3:
                            hand_card_number_list_copy[list[0]] = -1
                            hand_card_number_list_copy[list[1]] = -1
                            hand_card_number_list_copy[list[2]] = -1
                            score = score + 3
                        else:
                            pass
                        list = []
                    if (x == 2 or x == 3 or x == 12 or x == 13 or x == 22 or x == 23):
                        offset = offset + 1
                        for z in range(3):
                            for y in range(len(TRIPLET[xtriplet+1])):
                                if TRIPLET[xtriplet+1][y] in hand_card_number_list_copy:
                                    list.append(
                                        hand_card_number_list_copy.index(TRIPLET[xtriplet+1][y]))
                            if len(list) >= 3:
                                hand_card_number_list_copy[list[0]] = -1
                                hand_card_number_list_copy[list[1]] = -1
                                hand_card_number_list_copy[list[2]] = -1
                                score = score + 3
                            else:
                                pass
                            list = []

        for i in range(len(hand_card_number_list_copy)):
            if hand_card_number_list_copy[i] == -1:
                fourteen = fourteen + 1
        # print(f"{site}:{hand_card_number_list_copy}")
        # print(f"手牌能不能和：{fourteen}")
        # print(f"眼睛:{y_pair-1}\n")
        if fourteen == len(hand_card_number_list):
            print("\nyyyyyyyyyyyyy\n")
            return(True)
        if y_pair >= 37:
            break
    return(False)


def site_list_g(which, seed=1, index=0):
    site_list = []
    if which == "seed":
        if seed == 1:
            site_list = ["down", "left", "up", "right"]
        elif seed == 2:
            site_list = ["right", "down", "left", "up"]
        elif seed == 3:
            site_list = ["up", "right", "down", "left"]
        elif seed == 4:
            site_list = ["left", "up", "right", "down"]
        return site_list
    elif which == "index":
        if index == 0:
            site_list = ["down", "left", "up", "right"]
        elif index == 1:
            site_list = ["right", "down", "left", "up"]
        elif index == 2:
            site_list = ["up", "right", "down", "left"]
        elif index == 3:
            site_list = ["left", "up", "right", "down"]
        return site_list


def index_is_site(return_index, who_site):  # 哪家是誰的哪家
    #print("who: ", return_index, who_site)
    site_list = site_list_g("index", index=SITE_INDEX[who_site])
    #print("site list", site_list)
    return site_list[return_index]

################################################################################################################
# [主send socket,主recv socket,倒數send socket,倒數recv socket,name]


def play(client_list):
    print("start play")
    main_send_socket_list = [client_list[0][0], client_list[1][0], client_list[2][0], client_list[3][0]]
    main_recv_socket_list = [client_list[0][1], client_list[1][1], client_list[2][1], client_list[3][1]]
    sub_send_socket_list = [client_list[0][2], client_list[1][2], client_list[2][2], client_list[3][2]]
    sub_recv_socket_list = [client_list[0][3], client_list[1][3], client_list[2][3], client_list[3][3]]
    player_name_list = [client_list[0][4], client_list[1][4], client_list[2][4], client_list[3][4]]

    #####################################################
    GV = Global_variable()
    player1 = Player(player_name_list[0], "down")
    player2 = Player(player_name_list[1], "right")
    player3 = Player(player_name_list[2], "up")
    player4 = Player(player_name_list[3], "left")
    GV.player_list = [player1, player2, player3, player4]
    #####################################################
    single_data_recv_t0 = threading.Thread(target=single_data_recv, args=(GV, main_send_socket_list, main_recv_socket_list[0], 0))
    single_data_recv_t0.setDaemon(True)
    single_data_recv_t0.start()
    single_data_recv_t1 = threading.Thread(target=single_data_recv, args=(GV, main_send_socket_list, main_recv_socket_list[1], 1))
    single_data_recv_t1.setDaemon(True)
    single_data_recv_t1.start()
    single_data_recv_t2 = threading.Thread(target=single_data_recv, args=(GV, main_send_socket_list, main_recv_socket_list[2], 2))
    single_data_recv_t2.setDaemon(True)
    single_data_recv_t2.start()
    single_data_recv_t3 = threading.Thread(target=single_data_recv, args=(GV, main_send_socket_list, main_recv_socket_list[3], 3))
    single_data_recv_t3.setDaemon(True)
    single_data_recv_t3.start()
    countdown_recv_t0 = threading.Thread(target=countdown_recv, args=(GV, sub_recv_socket_list[0], player_name_list[0]))
    countdown_recv_t0.setDaemon(True)
    countdown_recv_t0.start()
    countdown_recv_t1 = threading.Thread(target=countdown_recv, args=(GV, sub_recv_socket_list[1], player_name_list[1]))
    countdown_recv_t1.setDaemon(True)
    countdown_recv_t1.start()
    countdown_recv_t2 = threading.Thread(target=countdown_recv, args=(GV, sub_recv_socket_list[2], player_name_list[2]))
    countdown_recv_t2.setDaemon(True)
    countdown_recv_t2.start()
    countdown_recv_t3 = threading.Thread(target=countdown_recv, args=(GV, sub_recv_socket_list[3], player_name_list[3]))
    countdown_recv_t3.setDaemon(True)
    countdown_recv_t3.start()

    do_not_add = 0
    target_river = ""
    chi_pong_kong_threads = []
    # if GV.MANAGER_MODE == 1:
    #    manager_define_process(GV,1)
    # 洗牌
    shuffle(GV)
    GV.MANAGE_MODE = 0  # 自訂手牌&抽牌
    if GV.MANAGE_MODE == 0:
        # 抓王牌七墩
        dora_mountain = Dora_Mountain()
        dora_mountain.dora_init(GV)
        dora_card = dora_mountain.flip_dora()

        # 決定順序(1為自己,2為下家(右邊),3為對家(上面),4為上家(左邊))
        # GV.SEED = random.randint(1, 4)
        GV.SEED = 1
        # 發牌
        GV.SEED = start_deal(GV, GV.player_list)
    else:
        # 決定順序(1為自己,2為下家(右邊),3為對家(上面),4為上家(左邊))
        # GV.SEED = random.randint(1, 4)
        GV.SEED = 1
        # 發牌
        GV.SEED = start_deal(GV, GV.player_list)

        # 抓王牌七墩
        dora_mountain = Dora_Mountain()
        dora_mountain.dora_init(GV)
        dora_card = dora_mountain.flip_dora()
        # if MANAGER_MODE == 0:

    # 排牌
    sort(GV.player_list)
    # 初始化send
    print("init start")
    data_num = "16"
    i = 0
    while i < 4:
        time.sleep(WAIT_TIME)
        main_send_socket_list[i].send(data_num.encode('utf-8'))  # 有幾筆資料
        #print(data_num)
        time.sleep(WAIT_TIME)
        main_send_socket_list[i].send("init".encode('utf-8'))  # 資料類別0
        #print("init")
        time.sleep(WAIT_TIME)
        main_send_socket_list[i].send(
            GV.player_list[i].site.encode('utf-8'))  # 風1
        #print(GV.player_list[i].site)
        time.sleep(WAIT_TIME)
        #print()
        j = 0
        while j < 13:
            main_send_socket_list[i].send(
                GV.player_list[i].card_list[j].encode('utf-8'))  # 13張手牌2~14
            #print(GV.player_list[i].card_list[j])
            time.sleep(WAIT_TIME)
            j += 1
        main_send_socket_list[i].send(dora_card.encode('utf-8'))  # 寶牌15
        #print()
        #print(dora_card)
        time.sleep(WAIT_TIME)
        #print()
        i += 1
    print("init end")
    # 遊戲流程
    while len(GV.CARD_MOUNTAIN) > 0:
        ###############################################
        data_num = "2"
        print("left_card_num start")
        i = 0
        while i < 4:
            main_send_socket_list[i].send(data_num.encode('utf-8'))  # 有幾筆資料
           #print(data_num)
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send(
                "left_card_num".encode('utf-8'))  # 資料類別0
           #print("left_card_num")
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send(
                str(len(GV.CARD_MOUNTAIN)-1).encode('utf-8'))  # 剩餘幾張牌
           #print(str(len(GV.CARD_MOUNTAIN)))
            time.sleep(WAIT_TIME)
           #print()
            i += 1
        print("left_card_num end")
        ###############################################

        if GV.LEAVE == 1:
            break

        countdown_socket_index = -1
        site_list = []
        if GV.SEED == 1:
            if GV.MANAGE_MODE == 1:
                player1.deal_card = GV.self_define_deal
                pass
            else:
                deal(GV, player1, "draw")

        elif GV.SEED == 2:
            if GV.MANAGE_MODE == 1:
                player2.deal_card = GV.self_define_deal
                pass
            else:
                deal(GV, player2, "draw")

        elif GV.SEED == 3:
            if GV.MANAGE_MODE == 1:
                player3.deal_card = GV.self_define_deal
                pass
            else:
                deal(GV, player3, "draw")

        elif GV.SEED == 4:
            if GV.MANAGE_MODE == 1:
                player4.deal_card = GV.self_define_deal
                pass
            else:
                deal(GV, player4, "draw")

        site_list = site_list_g("seed", GV.SEED)
        print(GV.SEED)
        # send抽牌
        i = 0
        data_num = "3"
        print("draw start")
        while i < 4:
            main_send_socket_list[i].send(data_num.encode('utf-8'))  # 有幾筆資料
           #print(data_num)
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send("draw".encode('utf-8'))  # 資料類別0
           #print("draw")
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send(
                site_list[i].encode('utf-8'))  # 哪家抽牌1
           #print(site_list[i])
            time.sleep(WAIT_TIME)
            if site_list[i] == "down":
                main_send_socket_list[i].send(
                    GV.player_list[i].deal_card.encode('utf-8'))  # 抽哪張2
               #print(GV.player_list[i].deal_card)
                countdown_socket_index = i
            else:
                main_send_socket_list[i].send("null".encode('utf-8'))
               #print("null")
           #print()
            i += 1
        print("draw end")
        # send抽牌end

        # 自摸
        iswin = can_win(GV, GV.player_list[countdown_socket_index].site,
                        GV.player_list[countdown_socket_index].deal_card)
        if iswin:
            print("tsumo start")
            time.sleep(WAIT_TIME)
            main_send_socket_list[countdown_socket_index].send(
                "2".encode('utf-8'))  # 有幾筆資料
           #print(1)
            time.sleep(WAIT_TIME)
            main_send_socket_list[countdown_socket_index].send(
                "tsumo".encode('utf-8'))  # 資料類別0
           #print("tsumo")
            time.sleep(WAIT_TIME)
            main_send_socket_list[countdown_socket_index].send(
                GV.player_list[countdown_socket_index].deal_card.encode('utf-8'))  # 摸哪張1
           #print(GV.player_list[countdown_socket_index].deal_card)
            print("tsumo end")
        # 自摸end
        print("append",GV.player_list[GV.SEED-1].deal_card)
        GV.player_list[GV.SEED-1].card_list.append(GV.player_list[GV.SEED-1].deal_card)
        deal_card = GV.player_list[GV.SEED-1].deal_card
        GV.player_list[GV.SEED-1].deal_card=""
        # 等待回覆或倒計時結束-出牌
        countdown_send(GV, sub_send_socket_list[countdown_socket_index],
                       sub_recv_socket_list[countdown_socket_index], player_name_list[countdown_socket_index])
        while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:
            pass
        if GV.LEAVE == 1:
            break
        GV.TIME_EVENT_SET = 0
        # GV.time_event.clear()
        # GV.IS_WAITING_DATA=True
        # GV.time_event.wait()
        # print("wait end")
        #print("get: ", GV.SEND_DATA[countdown_socket_index])

        # 如果自摸
        sort(GV.player_list)
        if GV.IS_WIN == 1:
            GV.IS_WIN = 0
            # 自摸那家的手牌跟副露總張數
            total_card_num = len(
                GV.player_list[countdown_socket_index].card_list)
            i = 0
            while i < len(GV.player_list[countdown_socket_index].vice_dews):
                total_card_num += len(
                    GV.player_list[countdown_socket_index].vice_dews[i])
                i += 1
            total_card_num += 1  # +CUT

            i = 0
            print("other_tsumo start")
            while i < 4:
                if i != countdown_socket_index:
                    time.sleep(WAIT_TIME)
                    data_num = str(3+total_card_num)
                    main_send_socket_list[i].send(
                        data_num.encode('utf-8'))  # 有幾筆資料
                   #print(data_num)
                    time.sleep(WAIT_TIME)
                    main_send_socket_list[i].send(
                        "other_tsumo".encode('utf-8'))  # 資料類別0
                   #print("other_tsumo")
                    time.sleep(WAIT_TIME)
                    main_send_socket_list[i].send(
                        site_list[i].encode('utf-8'))  # 誰自摸1
                   #print(site_list[i])
                    time.sleep(WAIT_TIME)
                    main_send_socket_list[i].send(
                        deal_card.encode('utf-8'))  # 摸哪張2
                   #print(GV.player_list[countdown_socket_index].deal_card)
                    time.sleep(WAIT_TIME)
                    j = 0
                    # 自摸那家的手牌
                    while j < len(GV.player_list[countdown_socket_index].card_list):
                        main_send_socket_list[i].send(
                            GV.player_list[countdown_socket_index].card_list[j].encode('utf-8'))
                       #print(GV.player_list[countdown_socket_index].card_list[j])
                        time.sleep(WAIT_TIME)
                        j += 1
                    main_send_socket_list[i].send(
                        "CUT".encode('utf-8'))  # CUT,用於分割手牌跟副露
                   #print("CUT")
                    time.sleep(WAIT_TIME)
                    j = 0
                    # 自摸那家的副露
                    while j < len(GV.player_list[countdown_socket_index].vice_dews):
                        k = 0
                        while k < len(GV.player_list[countdown_socket_index].vice_dews[j]):
                            main_send_socket_list[i].send(
                                GV.player_list[countdown_socket_index].vice_dews[j][k].encode('utf-8'))
                           #print(GV.player_list[countdown_socket_index].vice_dews[j][k])
                            time.sleep(WAIT_TIME)
                            k += 1
                        j += 1

                i += 1
            print("other_tsumo end")
            break
        # 如果自摸end
        elif GV.SEND_DATA[countdown_socket_index] == "":
            countdown_send(GV, sub_send_socket_list[countdown_socket_index],
                           sub_recv_socket_list[countdown_socket_index], player_name_list[countdown_socket_index])
            while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:
                pass
            if GV.LEAVE == 1:
                break
            GV.TIME_EVENT_SET = 0
        sort(GV.player_list)
        out_card = GV.SEND_DATA[countdown_socket_index]
        GV.SEND_DATA[countdown_socket_index] = ""
        GV.card_river.append(out_card)

        # GV.SEND_DATA[countdown_socket_index]#接收到的出牌的id

        # 回傳其他三家接到的牌
        i = 0
        data_num = "3"
        print("out start")
        while i < 4:
            if i != countdown_socket_index:
                main_send_socket_list[i].send(
                    data_num.encode('utf-8'))  # 有幾筆資料
               #print(data_num)
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send("out".encode('utf-8'))  # 資料類別0
               #print("out")
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(
                    site_list[i].encode('utf-8'))  # 哪家出牌1
               #print(site_list[i])
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(out_card.encode('utf-8'))  # 出哪張2
               #print(out_card)
                time.sleep(WAIT_TIME)
            i += 1
        print("out end")
        ################################################

        # 判斷3家是否可吃碰槓和 可以就傳送資料

        # 如果可以和
        win_index = -1
        i = 0
        
        while i < 4:
            if i != countdown_socket_index:
                iswin = can_win(GV, GV.player_list[i].site, out_card)
                if iswin:
                    print("ron start")
                    time.sleep(WAIT_TIME)
                    main_send_socket_list[i].send("2".encode('utf-8'))  # 有幾筆資料
                   #print(2)
                    time.sleep(WAIT_TIME)
                    main_send_socket_list[i].send(
                        "ron".encode('utf-8'))  # 資料類別0
                   #print("ron")
                    time.sleep(WAIT_TIME)
                    main_send_socket_list[i].send(
                        out_card.encode('utf-8'))  # 和哪張1
                    win_index = i
                    time.sleep(WAIT_TIME)
                    print("ron end")
                    break
            i += 1

        if iswin:
            sort(GV.player_list)
           #print("eeeeeee")
            countdown_send(
                GV, sub_send_socket_list[win_index], sub_recv_socket_list[win_index], player_name_list[win_index])
            while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:
                pass
            if GV.LEAVE == 1:
                break
            GV.TIME_EVENT_SET = 0
            # 等待資料end
            if GV.IS_WIN == 1:
                add_site_list = site_list_g("index", index=win_index)
                GV.IS_WIN = 0
                # 和那家的手牌跟副露總張數
                total_card_num = len(GV.player_list[win_index].card_list)
                i = 0
                while i < len(GV.player_list[win_index].vice_dews):
                    total_card_num += len(
                        GV.player_list[win_index].vice_dews[i])
                    i += 1
                total_card_num += 1  # +CUT

                i = 0
                print("other_ron start")
                while i < 4:
                    if i != win_index:
                        time.sleep(WAIT_TIME)
                        data_num = str(3+total_card_num)
                        main_send_socket_list[i].send(
                            data_num.encode('utf-8'))  # 有幾筆資料
                       #print(data_num)
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            "other_ron".encode('utf-8'))  # 資料類別0
                       #print("other_ron")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            add_site_list[i].encode('utf-8'))  # 誰和1
                       #print(add_site_list[i])
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            out_card.encode('utf-8'))  # 和哪張2
                       #print(out_card)
                        time.sleep(WAIT_TIME)
                        j = 0
                        while j < len(GV.player_list[win_index].card_list):  # 和那家的手牌
                            main_send_socket_list[i].send(
                                GV.player_list[win_index].card_list[j].encode('utf-8'))
                           #print(GV.player_list[win_index].card_list[j])
                            time.sleep(WAIT_TIME)
                            j += 1
                        main_send_socket_list[i].send(
                            "CUT".encode('utf-8'))  # CUT,用於分割手牌跟副露
                       #print("CUT")
                        time.sleep(WAIT_TIME)
                        j = 0
                        while j < len(GV.player_list[win_index].vice_dews):  # 和那家的副露
                            k = 0
                            while k < len(GV.player_list[win_index].vice_dews[j]):
                                main_send_socket_list[i].send(
                                    GV.player_list[win_index].vice_dews[j][k].encode('utf-8'))
                               #print(GV.player_list[win_index].vice_dews[j][k])
                                time.sleep(WAIT_TIME)
                                k += 1
                            j += 1

                    i += 1

                    # 如果和end
                print("other_ron end")
                break

        #print("如果可以和end")
        # 如果可以和end

        judge_win_card = ""  # 用於接吃碰槓的出牌來判斷是否和牌
        judge_out_index = -1  # 吃碰槓後的出牌家

        can_or_can_not_chi, target_cards_list = other_can_chi(
            GV, GV.player_list, GV.player_list[countdown_socket_index].site, out_card)  # can chi
        if can_or_can_not_chi and not iswin:  # 如果可以吃
            print("can_chi start")
            i = NEXT_SITE_INDEX[GV.player_list[countdown_socket_index].site]
            data_num = str(1+(2*len(target_cards_list)))
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send(data_num.encode('utf-8'))  # 有幾筆資料
           #print(data_num)
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send("can_chi".encode('utf-8'))  # 資料類別0
           #print("can_chi")
            time.sleep(WAIT_TIME)
            j = 0
            while j < len(target_cards_list):
                k = 0
                while k < len(target_cards_list[j]):
                    main_send_socket_list[i].send(
                        target_cards_list[j][k].encode('utf-8'))  # 哪些牌可以拿出來吃
                    time.sleep(WAIT_TIME)
                    k += 1
                j += 1
           #print()
            print("can_chi end")
           #print(GV.player_list[i].site, "can chi")
            countdown_send(
                GV, sub_send_socket_list[i], sub_recv_socket_list[i], player_name_list[i])
           #print("nimader", GV.TIME_EVENT_SET)
            while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:  # 等待資料
                pass
            if GV.LEAVE == 1:
                break
            GV.TIME_EVENT_SET = 0
           #print("nima")
            if GV.IS_CHI == 1:  # 回傳給其他三家 要刪除誰的牌河 誰吃
                GV.IS_CHI = 0
                del GV.card_river[len(GV.card_river)-1]
                add_site_list = site_list_g("index", index=i)
                j = 0
                print("other_chi start")
                while j < 4:
                    if j != i:
                        data_num = "6"
                        main_send_socket_list[j].send(
                            data_num.encode('utf-8'))  # 有幾筆資料
                       #print(data_num)
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            "other_chi".encode('utf-8'))  # 資料類別0
                       #print("other_chi")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            site_list[j].encode('utf-8'))  # 刪除誰家的牌河1
                       #print(site_list[j])
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            add_site_list[j].encode('utf-8'))  # 新增誰家的副露2
                       #print(site_list[j])
                        three_cards = GV.player_list[i].vice_dews[len(
                            GV.player_list[i].vice_dews)-1]
                        k = 0
                        while k < 3:
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                three_cards[k].encode('utf-8'))  # 新增哪三張
                            k += 1
                       #print(three_cards)
                    j += 1
                print("other_chi end")
                countdown_send(
                    GV, sub_send_socket_list[i], sub_recv_socket_list[i], player_name_list[i])
               #print("wait")
                while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:  # 等待出牌
                    pass
                if GV.LEAVE == 1:
                    break
                GV.TIME_EVENT_SET = 0
               #print("wait2")

                # 回傳其他三家接到的牌
                j = 0
                data_num = "3"
                print("out start")
                while j < 4:
                    if j != i:
                        main_send_socket_list[j].send(
                            data_num.encode('utf-8'))  # 有幾筆資料
                       #print(data_num)
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            "out".encode('utf-8'))  # 資料類別0
                       #print("out")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            add_site_list[j].encode('utf-8'))  # 哪家出牌1
                       #print(add_site_list[j])
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            GV.SEND_DATA[i].encode('utf-8'))  # 出哪張2
                       #print()
                    j += 1
                print("out end")
                ################################################

                GV.card_river.append(GV.SEND_DATA[i])
                judge_win_card = GV.SEND_DATA[i]
                judge_out_index = i
                GV.SEED += 1

        else:
            print("no chi")

        # NEXT_SITE_INDEX[GV.player_list[countdown_socket_index].site]#下一家的index
        can_or_can_not_pong_or_kong, can_what, index = others_can_pong_or_kong(
            GV, GV.player_list, GV.player_list[countdown_socket_index].site, out_card)  # can pong kong
        if can_or_can_not_pong_or_kong and not can_or_can_not_chi:  # 如果可以碰或槓 !!!偷懶
            print("can_pong_or_kong ",GV.player_list[index].card_list,GV.player_list[index].deal_card)
            if can_what == "CAN_PONG":
                i = index
                print("can_pong start")
                id = out_card
                site = index_is_site(
                    i, GV.player_list[countdown_socket_index].site)
                data_num = "3"
                main_send_socket_list[i].send(
                    data_num.encode('utf-8'))  # 有幾筆資料
               #print(data_num)
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(
                    "can_pong".encode('utf-8'))  # 資料類別0
               #print("can_pong")
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(site.encode('utf-8'))  # 可以碰哪家
               #print(site)
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(id.encode('utf-8'))  # 可以碰哪張
               #print(id)
                time.sleep(WAIT_TIME)
                print("can_pong end")
               #print(GV.player_list[i].site, "can pong")
                countdown_send(
                    GV, sub_send_socket_list[i], sub_recv_socket_list[i], player_name_list[i])
               #print("nimader pong", GV.TIME_EVENT_SET)
                while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:  # 等待資料
                    pass
                if GV.LEAVE == 1:
                    break
                GV.TIME_EVENT_SET = 0
               #print("nima pong")
                # GV.player_list[index]#可以碰的那一家

                if GV.IS_PONG == 1:  # 回傳給其他三家 要刪除誰的牌河 誰碰
                    GV.IS_PONG = 0
                    del GV.card_river[len(GV.card_river)-1]
                    add_site_list = site_list_g("index", index=i)
                    j = 0
                    print("other_pong start")
                    while j < 4:
                        if j != i:
                            data_num = "4"
                            main_send_socket_list[j].send(
                                data_num.encode('utf-8'))  # 有幾筆資料
                           #print(data_num)
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                "other_pong".encode('utf-8'))  # 資料類別0
                           #print("other_pong")
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                site_list[j].encode('utf-8'))  # 刪除誰家的牌河1
                           #print(site_list[j])
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                add_site_list[j].encode('utf-8'))  # 新增誰家的副露2
                           #print(add_site_list[j])
                            three_cards = GV.player_list[i].vice_dews[len(
                                GV.player_list[i].vice_dews)-1]
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                three_cards[0].encode('utf-8'))  # 新增哪一張*3 3
                           #print(three_cards[0])
                        j += 1
                    print("other_pong end")
                    countdown_send(
                        GV, sub_send_socket_list[i], sub_recv_socket_list[i], player_name_list[i])
                   #print("wait pong out")
                    while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:  # 等待出牌
                        pass
                    if GV.LEAVE == 1:
                        break
                    GV.TIME_EVENT_SET = 0
                   #print("wait pong out2")

                    # 回傳其他三家接到的牌
                    j = 0
                    data_num = "3"
                    print("out start")
                    while j < 4:
                        if j != i:
                            main_send_socket_list[j].send(
                                data_num.encode('utf-8'))  # 有幾筆資料
                           #print(data_num)
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                "out".encode('utf-8'))  # 資料類別0
                           #print("out")
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                add_site_list[j].encode('utf-8'))  # 哪家出牌1
                           #print(add_site_list[j])
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                GV.SEND_DATA[i].encode('utf-8'))  # 出哪張2
                           #print()
                        j += 1
                    print("out end")
                    ################################################
                    GV.card_river.append(GV.SEND_DATA[i])
                    judge_win_card = GV.SEND_DATA[i]
                    judge_out_index = i
                    GV.SEED = i+1

            elif can_what == "CAN_PONG_AND_KONG":
                print("can_pong_and_kong start")
                i = index
                id = out_card
                site = index_is_site(
                    i, GV.player_list[countdown_socket_index].site)
                data_num = "3"
                main_send_socket_list[i].send(
                    data_num.encode('utf-8'))  # 有幾筆資料
               #print(data_num)
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(
                    "can_pong_and_kong".encode('utf-8'))  # 資料類別0
               #print("can_pong_and_kong")
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(site.encode('utf-8'))  # 可以碰槓哪家
               #print(site)
                time.sleep(WAIT_TIME)
                main_send_socket_list[i].send(id.encode('utf-8'))  # 可以碰槓哪張
               #print(id)
                time.sleep(WAIT_TIME)
                print("can_pong_and_kong end")
               #print(GV.player_list[i].site, "can pong and kong")
                countdown_send(
                    GV, sub_send_socket_list[i], sub_recv_socket_list[i], player_name_list[i])
               #print("nimader pong kong", GV.TIME_EVENT_SET)
                while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:  # 等待資料
                    pass
                if GV.LEAVE == 1:
                    break
                GV.TIME_EVENT_SET = 0
               #print("nima pong kong")
                # GV.player_list[index]#可以碰槓的那一家

                if GV.IS_PONG == 1:  # 回傳給其他三家 要刪除誰的牌河 誰碰
                    GV.IS_PONG = 0
                    del GV.card_river[len(GV.card_river)-1]
                    add_site_list = site_list_g("index", index=i)
                    j = 0
                    print("other_pong start")
                    while j < 4:
                        if j != i:
                            data_num = "4"
                            main_send_socket_list[j].send(
                                data_num.encode('utf-8'))  # 有幾筆資料
                           #print(data_num)
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                "other_pong".encode('utf-8'))  # 資料類別0
                           #print("other_pong")
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                site_list[j].encode('utf-8'))  # 刪除誰家的牌河1
                           #print(site_list[j])
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                add_site_list[j].encode('utf-8'))  # 新增誰家的副露2
                           #print(add_site_list[j])
                            three_cards = GV.player_list[i].vice_dews[len(
                                GV.player_list[i].vice_dews)-1]
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                three_cards[0].encode('utf-8'))  # 新增哪一張*3 3
                           #print(three_cards[0])
                        j += 1
                    print("other_pong end")
                    countdown_send(
                        GV, sub_send_socket_list[i], sub_recv_socket_list[i], player_name_list[i])
                   #print("wait pong out3")
                    while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:  # 等待出牌
                        pass
                    if GV.LEAVE == 1:
                        break
                    GV.TIME_EVENT_SET = 0
                   #print("wait pong out4")

                    # 回傳其他三家接到的牌
                    j = 0
                    data_num = "3"
                    print("out start")
                    while j < 4:
                        if j != i:
                            main_send_socket_list[j].send(
                                data_num.encode('utf-8'))  # 有幾筆資料
                           #print(data_num)
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                "out".encode('utf-8'))  # 資料類別0
                           #print("out")
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                add_site_list[j].encode('utf-8'))  # 哪家出牌1
                           #print(add_site_list[j])
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                GV.SEND_DATA[i].encode('utf-8'))  # 出哪張2
                           #print()
                        j += 1
                    print("out end")
                    ################################################
                    GV.card_river.append(GV.SEND_DATA[i])
                    judge_win_card = GV.SEND_DATA[i]
                    judge_out_index = i
                    GV.SEED = i+1

                elif GV.IS_KONG == 1:
                    GV.IS_KONG = 0
                    # 回傳給其他三家 要刪除誰的牌河 誰槓
                    del GV.card_river[len(GV.card_river)-1]
                    add_site_list = site_list_g("index", index=i)
                    j = 0
                    print("other_kong start")
                    while j < 4:
                        if j != i:
                            data_num = "4"
                            main_send_socket_list[j].send(
                                data_num.encode('utf-8'))  # 有幾筆資料
                           #print(data_num)
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                "other_kong".encode('utf-8'))  # 資料類別0
                           #print("other_kong")
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                site_list[j].encode('utf-8'))  # 刪除誰家的牌河1
                           #print(site_list[j])
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                add_site_list[j].encode('utf-8'))  # 新增誰家的副露2
                           #print(add_site_list[j])
                            four_cards = GV.player_list[i].vice_dews[len(
                                GV.player_list[i].vice_dews)-1]
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                four_cards[0].encode('utf-8'))  # 新增哪一張*4 3
                           #print(four_cards[0])
                        j += 1
                    print("other_kong end")
                    # send抽牌(#回傳槓上牌)
                    dora_mountain.deal(GV, GV.player_list[i].site)  # 槓上抽牌
                    GV.player_list[i].card_list.append(GV.player_list[i].deal_card)
                    deal_card = GV.player_list[i].deal_card
                    GV.player_list[i].deal_card=""
                    add_site_list = site_list_g("index", index=i)
                    j = 0
                    data_num = "3"
                    print("draw start")
                    while j < 4:
                        main_send_socket_list[j].send(
                            data_num.encode('utf-8'))  # 有幾筆資料
                       #print(data_num)
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            "draw".encode('utf-8'))  # 資料類別0
                       #print("draw")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            add_site_list[j].encode('utf-8'))  # 哪家抽牌1
                       #print(add_site_list[j])
                        time.sleep(WAIT_TIME)
                        if add_site_list[j] == "down":
                           #print("槓上抽牌", GV.player_list[j].deal_card)
                            main_send_socket_list[j].send(
                                deal_card.encode('utf-8'))  # 抽哪張2
                           #print(GV.player_list[j].deal_card)
                            # countdown_socket_index=j
                        else:
                            main_send_socket_list[j].send(
                                "null".encode('utf-8'))
                           #print("null")
                        time.sleep(WAIT_TIME)
                       #print()
                        j += 1
                    print("draw end")
                    # 判斷嶺上開花
                    iswin = can_win(
                        GV, GV.player_list[i].site, deal_card)
                    if iswin:
                        print("tsumo start")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            "2".encode('utf-8'))  # 有幾筆資料
                       #print(1)
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            "tsumo".encode('utf-8'))  # 資料類別0
                       #print("tsumo")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            deal_card.encode('utf-8'))  # 摸哪張1
                       #print(GV.player_list[i].deal_card)
                        time.sleep(WAIT_TIME)
                        print("tsumo end")
                    # 判斷嶺上開花end

                    # 等待資料(槓打牌或開花)
                    countdown_send(
                        GV, sub_send_socket_list[i], sub_recv_socket_list[i], player_name_list[i])
                   #print("nimader 槓打牌或開花", GV.TIME_EVENT_SET)
                    while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:  # 等待資料
                        pass
                    if GV.LEAVE == 1:
                        break
                    GV.TIME_EVENT_SET = 0
                   #print("nima 槓打牌或開花")
                    # 等待資料(槓打牌或開花)end

                    # 如果嶺上開花
                    if GV.IS_WIN == 1:
                        GV.IS_WIN = 0
                        countdown_socket_index = i
                        # 自摸那家的手牌跟副露總張數
                        total_card_num = len(
                            GV.player_list[countdown_socket_index].card_list)
                        i = 0
                        while i < len(GV.player_list[countdown_socket_index].vice_dews):
                            total_card_num += len(
                                GV.player_list[countdown_socket_index].vice_dews[i])
                            i += 1
                        total_card_num += 1  # +CUT

                        i = 0
                        print("other_tsumo start")
                        while i < 4:
                            if i != countdown_socket_index:
                                time.sleep(WAIT_TIME)
                                data_num = str(3+total_card_num)
                                main_send_socket_list[i].send(
                                    data_num.encode('utf-8'))  # 有幾筆資料
                               #print(data_num)
                                time.sleep(WAIT_TIME)
                                main_send_socket_list[i].send(
                                    "other_tsumo".encode('utf-8'))  # 資料類別0
                               #print("other_tsumo")
                                time.sleep(WAIT_TIME)
                                main_send_socket_list[i].send(
                                    site_list[i].encode('utf-8'))  # 誰自摸1
                               #print(site_list[i])
                                time.sleep(WAIT_TIME)
                                main_send_socket_list[i].send(
                                    deal_card.encode('utf-8'))  # 摸哪張2
                               #print( GV.player_list[countdown_socket_index].deal_card)
                                time.sleep(WAIT_TIME)
                                j = 0
                                # 自摸那家的手牌
                                while j < len(GV.player_list[countdown_socket_index].card_list):
                                    main_send_socket_list[i].send(
                                        GV.player_list[countdown_socket_index].card_list[j].encode('utf-8'))
                                   #print(GV.player_list[countdown_socket_index].card_list[j])
                                    time.sleep(WAIT_TIME)
                                    j += 1
                                main_send_socket_list[i].send(
                                    "CUT".encode('utf-8'))  # CUT,用於分割手牌跟副露
                               #print("CUT")
                                time.sleep(WAIT_TIME)
                                j = 0
                                # 自摸那家的副露
                                while j < len(GV.player_list[countdown_socket_index].vice_dews):
                                    k = 0
                                    while k < len(GV.player_list[countdown_socket_index].vice_dews[j]):
                                        main_send_socket_list[i].send(
                                            GV.player_list[countdown_socket_index].vice_dews[j][k].encode('utf-8'))
                                       #print(GV.player_list[countdown_socket_index].vice_dews[j][k])
                                        time.sleep(WAIT_TIME)
                                        k += 1
                                    j += 1

                            i += 1
                        print("other_tsumo end")
                        break

                    # 如果嶺上開花end

                    # 回傳其他三家接到的牌
                    j = 0
                    data_num = "3"
                    print("out start")
                    while j < 4:
                        if j != i:
                            main_send_socket_list[j].send(
                                data_num.encode('utf-8'))  # 有幾筆資料
                           #print(data_num)
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                "out".encode('utf-8'))  # 資料類別0
                           #print("out")
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                add_site_list[j].encode('utf-8'))  # 哪家出牌1
                           #print(add_site_list[j])
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[j].send(
                                GV.SEND_DATA[i].encode('utf-8'))  # 出哪張2
                           #print()
                        j += 1
                    print("out end")
                    ################################################

                    # 回傳寶牌翻牌給四家
                    dora_card = dora_mountain.flip_dora()
                    j = 0
                    print("flip_dora start")
                    while j < 4:
                        data_num = "2"
                        main_send_socket_list[j].send(
                            data_num.encode('utf-8'))  # 有幾筆資料
                       #print(data_num)
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            "flip_dora".encode('utf-8'))  # 資料類別0
                       #print("flip_dora")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[j].send(
                            dora_card.encode('utf-8'))  # 寶牌翻到哪張1
                       #print(dora_card)
                        time.sleep(WAIT_TIME)
                        j += 1
                    print("flip_dora end")
                    # countdown_send(GV,sub_send_socket_list[i],sub_recv_socket_list[i],player_name_list[i])
                    # print("wait kong out")
                    # while GV.TIME_EVENT_SET == 0 and GV.LEAVE==0:#等待出牌
                    #	pass
                    # if GV.LEAVE==1:
                    #	break
                    # GV.TIME_EVENT_SET=0
                    # print("wait kong out2")

                    GV.card_river.append(GV.SEND_DATA[i])
                    judge_win_card = GV.SEND_DATA[i]
                    judge_out_index = i
                    GV.SEED = i+1

                # GV.player_list[index]#可以碰/槓的那一家
        else:
            print("no pong kong")
        sort(GV.player_list)
        if judge_win_card != "":  # 不為空就需要判斷can_win
            # 如果可以和
            win_index = -1
            i = 0
            
            while i < 4:
                if i != judge_out_index:
                    iswin = can_win(GV, GV.player_list[i].site, judge_win_card)
                    if iswin:
                        print("ron start")
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            "1".encode('utf-8'))  # 有幾筆資料
                       #print(2)
                        time.sleep(WAIT_TIME)
                        main_send_socket_list[i].send(
                            "ron".encode('utf-8'))  # 資料類別0
                        win_index = i
                        print("ron end")
                        break
                i += 1

            if iswin:
                countdown_send(
                    GV, sub_send_socket_list[win_index], sub_recv_socket_list[win_index], player_name_list[win_index])
                while GV.TIME_EVENT_SET == 0 and GV.LEAVE == 0:
                    pass
                if GV.LEAVE == 1:
                    break
                GV.TIME_EVENT_SET = 0
                # 等待資料end
                if GV.IS_WIN == 1:
                    add_site_list = site_list_g("index", index=win_index)
                    GV.IS_WIN = 0
                    # 和那家的手牌跟副露總張數
                    total_card_num = len(GV.player_list[win_index].card_list)
                    i = 0
                    while i < len(GV.player_list[win_index].vice_dews):
                        total_card_num += len(
                            GV.player_list[win_index].vice_dews[i])
                        i += 1
                    total_card_num += 1  # +CUT

                    i = 0
                    print("other_ron start")
                    while i < 4:
                        if i != win_index:
                            time.sleep(WAIT_TIME)
                            data_num = str(3+total_card_num)
                            main_send_socket_list[i].send(
                                data_num.encode('utf-8'))  # 有幾筆資料
                           #print(data_num)
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[i].send(
                                "other_ron".encode('utf-8'))  # 資料類別0
                           #print("other_ron")
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[i].send(
                                add_site_list[i].encode('utf-8'))  # 誰和1
                           #print(add_site_list[i])
                            time.sleep(WAIT_TIME)
                            main_send_socket_list[i].send(
                                judge_win_card.encode('utf-8'))  # 和哪張2
                           #print(judge_win_card)
                            time.sleep(WAIT_TIME)
                            j = 0
                            # 和那家的手牌
                            while j < len(GV.player_list[win_index].card_list):
                                main_send_socket_list[i].send(
                                    GV.player_list[win_index].card_list[j].encode('utf-8'))
                               #print(GV.player_list[win_index].card_list[j])
                                time.sleep(WAIT_TIME)
                                j += 1
                            main_send_socket_list[i].send(
                                "CUT".encode('utf-8'))  # CUT,用於分割手牌跟副露
                           #print("CUT")
                            time.sleep(WAIT_TIME)
                            j = 0
                            # 和那家的副露
                            while j < len(GV.player_list[win_index].vice_dews):
                                k = 0
                                while k < len(GV.player_list[win_index].vice_dews[j]):
                                    main_send_socket_list[i].send(
                                        GV.player_list[win_index].vice_dews[j][k].encode('utf-8'))
                                   #print(GV.player_list[win_index].vice_dews[j][k])
                                    time.sleep(WAIT_TIME)
                                    k += 1
                                j += 1

                        i += 1

                        # 如果和end
                    print("other_ron end")
                    break

            # 如果可以和end

        #################
        # print("wait")
        # GV.time_event.clear()
        # GV.IS_WAITING_DATA=True
        # GV.time_event.wait()
        # print("wait end")

        GV.SEED += 1
        if GV.SEED == 5:
            GV.SEED = 1
        elif GV.SEED == 6:
            GV.SEED = 2
        print("NEXT ROUND:", GV.SEED)
    
    GV.SEND_FINISH = 1
    if len(GV.CARD_MOUNTAIN)<=0:
        i=0
        data_num="1"
        while i<4:
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send(data_num.encode('utf-8'))  # 有幾筆資料
            #print(data_num)
            time.sleep(WAIT_TIME)
            main_send_socket_list[i].send("no_result_end".encode('utf-8'))  # 資料類別0
            #print("no_result_end")
            i += 1
        
    print("game over")
    time.sleep(0.5)
    end_socket_processing(player_name_list)
    print("桌結束")


# 傳
# 有幾筆資料要收
# [誰 做了甚麼 動作][誰][資料][誰][資料][誰][資料][誰][資料]
# [誰(傳送目標方向的某家),動作,[傳送目標方向的資料,傳送目標下家的資料,傳送目標對家的資料,傳送目標上家的資料]]
# 動作:
# 抽牌


# wait_client_t = threading.Thread(target=wait_client)
# wait_client_t.setDaemon(True)
# wait_client_t.start()
TRIPLET = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [2, 3, 5], [3, 4, 6], [3, 5, 6], [4, 6, 7], [5, 6, 7], [6, 7, 8], [7, 8, 9], [10, 11, 12], [11, 12, 13],
           [12, 13, 14], [12, 13, 15], [13, 14, 16], [13, 15, 16], [14, 16, 17], [
    15, 16, 17], [16, 17, 18], [17, 18, 19], [20, 21, 22],
    [21, 22, 23], [22, 23, 24], [22, 23, 25], [23, 24, 26], [23, 25, 26], [24, 26, 27], [25, 26, 27], [26, 27, 28], [27, 28, 29]]
# 判斷對子跟刻子是一樣的
SEQUENCE = [[0], [1], [2], [3], [4, 5], [6], [7], [8], [9], [10], [11], [12], [13], [14, 15], [16], [17], [18],
            [19], [20], [21], [22], [23], [24], [24, 25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36]]

TWO_SITE = [[1, 2], [2, 3], [3, 4], [3, 5], [4, 6], [5, 6], [6, 7], [7, 8], [11, 12], [12, 13], [13, 14], [13, 15], [14, 16],
            [15, 16], [16, 17], [17, 18], [21, 22], [22, 23], [23, 24], [23, 25], [24, 26], [25, 26], [26, 27], [27, 28]]
# 中張
MIDDLE = [[1, 3], [2, 4], [2, 5], [3, 6], [4, 7], [5, 7], [6, 8], [11, 13], [12, 14], [12, 15], [13, 16], [14, 17],
          [15, 17], [16, 18], [21, 23], [22, 24], [22, 25], [23, 26], [24, 27], [25, 27], [26, 28]]

# 么九
ONE_SITE = [[0, 1], [0, 2], [7, 9], [8, 9], [10, 11], [10, 12],
            [17, 19], [18, 19], [20, 21], [20, 22], [27, 29], [28, 29]]
ZERO_SITE = [[0, 1, 2], [7, 8, 9], [10, 11, 12],
             [17, 18, 19], [20, 21, 22], [27, 28, 29]]
# 三元
R_G_W = [[34], [35], [36]]
# 風牌
E_S_W_T = [[30], [31], [32], [33]]
# 一氣
ONE_TO_NINE = [[0, 1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 16, 17, 18, 19],
               [10, 11, 12, 13, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 26, 27, 28, 29], [20, 21, 22, 23, 25, 26, 27, 28, 29]]
# 三色
TRIPLE_THREE = []
# 國士
NINE_AND_NINE = [[0], [9], [10], [19], [20], [
    29], [30], [31], [32], [33], [34], [35], [36]]
# 出牌順序
ORDER = [30, 31, 32, 33, 34, 35, 36, 0, 9, 10, 19, 20, 29, 1, 8, 11, 18, 21, 28, 2, 3, 5, 4, 6, 7, 12, 13, 15, 14, 16,
         17, 22, 23, 25, 24, 26, 27]
ORDER_TEXT = ["Ton", "Nan", "Shaa", "Pei", "Chun", "Haku", "Hatsu", "Man1", "Man9", "Pin1", "Pin9", "Sou1", "Sou9", "Man2", "Man8", "Pin2", "Pin8", "Sou2", "Sou8",
              "Man3", "Man4", "Man5_red", "Man5", "Man6", "Man7", "Pin3", "Pin4", "Pin5_red", "Pin5", "Pin6", "Pin7", "Sou3", "Sou4", "Sou5_red", "Sou5", "Sou6", "Sou7", ]


class Player:
    def __init__(self, username, site):
        self.user_name = username
        self.site = site  # 風,down,right,up,left
        self.point = 25000
        self.card_list = []  # id手牌13張
        self.deal_card = ""  # id剛抽的牌
        self.vice_dews = []  # id副露


class Global_variable:
    def __init__(self):
        self.SEND_FINISH = 0
        # 自訂手牌(13張)
        self.self_define_card1 = ["Man1", "Man1", "Man1", "Man4", "Man4",
                                  "Man4", "Man7", "Man7", "Man7", "Pin1", "Pin4", "Pin5", "Pin6"]
        self.self_define_card2 = ["Man2", "Man2", "Man2", "Man5", "Man5",
                                  "Man5", "Man8", "Man8", "Man8", "Pin2", "Pin2", "Pin2", "Pin7"]
        self.self_define_card3 = ["Man3", "Man3", "Man3", "Man6", "Man6",
                                  "Man6", "Man9", "Man9", "Man9", "Pin3", "Pin3", "Pin3", "Pin6"]
        self.self_define_card4 = ["Man1", "Pin1", "Man3", "Man4", "Pin5",
                                  "Man6", "Man7", "Man8", "Man9", "Pin1", "Pin2", "Pin3", "Pin4"]
        self.self_define_cards = [
            self.self_define_card1, self.self_define_card2, self.self_define_card3, self.self_define_card4]
        # 自訂手牌end
        # 自訂抽牌
        self.self_define_deal = "Pin7"
        # 自訂抽牌end
        self.MANAGE_MODE = 0
        # 流程
        self.SEED = 1
        # 四家傳送過來的資料
        self.DATA_LIST = [[], [], [], []]
        self.SEND_DATA = ["", "", "", ""]  # 四家出牌id
        self.time_event = threading.Event()
        self.condition_event = threading.Condition()
        self.IS_WAITING_DATA = False
        self.CAN_CHI = [0, 0, 0, 0]
        self.CAN_PONG = [0, 0, 0, 0]
        self.CAN_KONG = [0, 0, 0, 0]
        self.TIME_EVENT_SET = 0
        self.IS_COUNTDOWN_FINISH = 0
        self.LEAVE = 0
        self.player_list = []
        self.card_river = []
        self.IS_CHI = 0
        self.IS_PONG = 0
        self.IS_KONG = 0
        self.IS_WIN = 0
        # 剩餘麻將列表
        self.REMAINING_MAHJONG_LIST = ["Man1", "Man1", "Man1", "Man1", "Man2", "Man2", "Man2", "Man2", "Man3", "Man3", "Man3", "Man3", "Man4", "Man4", "Man4", "Man4", "Man5", "Man5", "Man5", "Man6", "Man6", "Man6", "Man6", "Man7", "Man7", "Man7", "Man7", "Man8", "Man8", "Man8", "Man8", "Man9", "Man9", "Man9", "Man9", "Pin1", "Pin1", "Pin1", "Pin1", "Pin2", "Pin2", "Pin2", "Pin2", "Pin3", "Pin3", "Pin3", "Pin3", "Pin4", "Pin4", "Pin4", "Pin4", "Pin5", "Pin5", "Pin5", "Pin6", "Pin6", "Pin6", "Pin6", "Pin7", "Pin7", "Pin7", "Pin7", "Pin8", "Pin8", "Pin8", "Pin8", "Pin9",
                                       "Pin9", "Pin9", "Pin9", "Sou1", "Sou1", "Sou1", "Sou1", "Sou2", "Sou2", "Sou2", "Sou2", "Sou3", "Sou3", "Sou3", "Sou3", "Sou4", "Sou4", "Sou4", "Sou4", "Sou5", "Sou5", "Sou5", "Sou6", "Sou6", "Sou6", "Sou6", "Sou7", "Sou7", "Sou7", "Sou7", "Sou8", "Sou8", "Sou8", "Sou8", "Sou9", "Sou9", "Sou9", "Sou9", "Ton", "Ton", "Ton", "Ton", "Nan", "Nan", "Nan", "Nan", "Shaa", "Shaa", "Shaa", "Shaa", "Pei", "Pei", "Pei", "Pei", "Chun", "Chun", "Chun", "Chun", "Haku", "Haku", "Haku", "Haku", "Hatsu", "Hatsu", "Hatsu", "Hatsu", "Man5_red", "Pin5_red", "Sou5_red"]

        # 牌山
        self.CARD_MOUNTAIN = []

        # 牌山
        # 王牌
        ################
        self.WIDTH = 1280  # 寬
        self.HEIGHT = 720  # 高
        self.MAHJONG_WIDTH = 51
        self.MAHJONG_HEIGHT = 68
        self.SMALL_MAHJONG_WIDTH = 36
        self.SMALL_MAHJONG_HEIGHT = 48
        self.MANAGER_MODE = 0  # 自訂模式
        self.BACK_OR_FRONT = True
        if self.MANAGER_MODE == 1:
            self.BACK_OR_FRONT = False
        self.HAND_CARDS_STARTX = 260  # 最右邊手牌x座標
        self.HAND_CARDS_STARTY = 640  # 最右邊手牌y座標
        self.RIGHT_HAND_CARD_STARTX = 1080  # 最右邊手牌x座標 下家
        self.RIGHT_HAND_CARD_STARTY = 560  # 最右邊手牌y座標 下家
        self.UP_HAND_CARD_STARTX = 840  # 最右邊手牌x座標 對家
        self.UP_HAND_CARD_STARTY = 20  # 最右邊手牌y座標 對家
        self.LEFT_HAND_CARD_STARTX = 154  # 最右邊手牌x座標 上家
        self.LEFT_HAND_CARD_STARTY = 128  # 最右邊手牌y座標 上家
        self.DEAL_CARD = []
        self.SMALL_DEAL_CARD = []
        self.IS_SHOW_COUNTDOWN = 0  # 是否要顯示倒計時
        self.COUNTDOWN_TIME = 0  # 剩餘秒數

        # 和牌方向 只會固定一次
        # self.ROAD_DOWN = -1
        # self.ROAD_RIGHT = 6
        # self.ROAD_UP = 6
        # self.ROAD_LEFT = 6

        # 三家鳴牌區
        self.RIGHT_VICE_DEWS = []  # [[這一張的x,下一張的y,小麻將物件], ...]
        self.UP_VICE_DEWS = []  # [[下一張的x,這(下)一張的y,小麻將物件], ...]
        self.LEFT_VICE_DEWS = []  # [[這(下)一張的x,這一張的y,小麻將物件], ...]
        self.RIGHT_VICE_DEWS_START_X = self.WIDTH - self.SMALL_MAHJONG_HEIGHT
        self.RIGHT_VICE_DEWS_START_Y = 0
        self.UP_VICE_DEWS_START_X = 200
        self.UP_VICE_DEWS_START_Y = 0
        self.LEFT_VICE_DEWS_START_X = 0
        self.LEFT_VICE_DEWS_START_Y = self.HEIGHT

        self.VICE_DEWS_BUTTON_LIST = []
        self.VICE_DEWS_BUTTON_STARTX = 430
        self.VICE_DEWS_BUTTON_STARTY = 480
        self.VICE_DEWS_BG_WIDTH = 108
        self.VICE_DEWS_BG_HEIGHT = 72

        # 麻將圖片字典
        # self.MAHJONG_IMG_DICT = {"Man1": Man1_img, "Man2": Man2_img, "Man3": Man3_img, "Man4": Man4_img, "Man5": Man5_img, "Man6": Man6_img, "Man7": Man7_img, "Man8": Man8_img, "Man9": Man9_img, "Pin1": Pin1_img, "Pin2": Pin2_img, "Pin3": Pin3_img, "Pin4": Pin4_img, "Pin5": Pin5_img, "Pin6": Pin6_img, "Pin7": Pin7_img, "Pin8": Pin8_img, "Pin9": Pin9_img, "Sou1": Sou1_img,
        #			"Sou2": Sou2_img, "Sou3": Sou3_img, "Sou4": Sou4_img, "Sou5": Sou5_img, "Sou6": Sou6_img, "Sou7": Sou7_img, "Sou8": Sou8_img, "Sou9": Sou9_img, "Ton": Ton_img, "Nan": Nan_img, "Shaa": Shaa_img, "Pei": Pei_img, "Chun": Chun_img, "Haku": Haku_img, "Hatsu": Hatsu_img, "Man5_red": Man5_red_img, "Pin5_red": Pin5_red_img, "Sou5_red": Sou5_red_img}
        # self.SMALL_MAHJONG_IMG_DICT = {"back": {"down":back_img,"right":back_right_img,"up":back_up_img,"left":back_left_img}, "Man1": {"small": small_Man1_img, "small_right": small_right_Man1_img, "small_up": small_up_Man1_img, "small_left": small_left_Man1_img}, "Man2": {"small": small_Man2_img, "small_right": small_right_Man2_img, "small_up": small_up_Man2_img, "small_left": small_left_Man2_img}, "Man3": {"small": small_Man3_img, "small_right": small_right_Man3_img, "small_up": small_up_Man3_img, "small_left": small_left_Man3_img}, "Man4": {"small": small_Man4_img, "small_right": small_right_Man4_img, "small_up": small_up_Man4_img, "small_left": small_left_Man4_img}, "Man5": {"small": small_Man5_img, "small_right": small_right_Man5_img, "small_up": small_up_Man5_img, "small_left": small_left_Man5_img}, "Man6": {"small": small_Man6_img, "small_right": small_right_Man6_img, "small_up": small_up_Man6_img, "small_left": small_left_Man6_img}, "Man7": {"small": small_Man7_img, "small_right": small_right_Man7_img, "small_up": small_up_Man7_img, "small_left": small_left_Man7_img}, "Man8": {"small": small_Man8_img, "small_right": small_right_Man8_img, "small_up": small_up_Man8_img, "small_left": small_left_Man8_img}, "Man9": {"small": small_Man9_img, "small_right": small_right_Man9_img, "small_up": small_up_Man9_img, "small_left": small_left_Man9_img}, "Pin1": {"small": small_Pin1_img, "small_right": small_right_Pin1_img, "small_up": small_up_Pin1_img, "small_left": small_left_Pin1_img}, "Pin2": {"small": small_Pin2_img, "small_right": small_right_Pin2_img, "small_up": small_up_Pin2_img, "small_left": small_left_Pin2_img}, "Pin3": {"small": small_Pin3_img, "small_right": small_right_Pin3_img, "small_up": small_up_Pin3_img, "small_left": small_left_Pin3_img}, "Pin4": {"small": small_Pin4_img, "small_right": small_right_Pin4_img, "small_up": small_up_Pin4_img, "small_left": small_left_Pin4_img}, "Pin5": {"small": small_Pin5_img, "small_right": small_right_Pin5_img, "small_up": small_up_Pin5_img, "small_left": small_left_Pin5_img}, "Pin6": {"small": small_Pin6_img, "small_right": small_right_Pin6_img, "small_up": small_up_Pin6_img, "small_left": small_left_Pin6_img}, "Pin7": {"small": small_Pin7_img, "small_right": small_right_Pin7_img, "small_up": small_up_Pin7_img, "small_left": small_left_Pin7_img}, "Pin8": {"small": small_Pin8_img, "small_right": small_right_Pin8_img, "small_up": small_up_Pin8_img, "small_left": small_left_Pin8_img}, "Pin9": {"small": small_Pin9_img, "small_right": small_right_Pin9_img, "small_up": small_up_Pin9_img, "small_left": small_left_Pin9_img}, "Sou1": {"small": small_Sou1_img, "small_right": small_right_Sou1_img,
        #																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																									   "small_up": small_up_Sou1_img, "small_left": small_left_Sou1_img}, "Sou2": {"small": small_Sou2_img, "small_right": small_right_Sou2_img, "small_up": small_up_Sou2_img, "small_left": small_left_Sou2_img}, "Sou3": {"small": small_Sou3_img, "small_right": small_right_Sou3_img, "small_up": small_up_Sou3_img, "small_left": small_left_Sou3_img}, "Sou4": {"small": small_Sou4_img, "small_right": small_right_Sou4_img, "small_up": small_up_Sou4_img, "small_left": small_left_Sou4_img}, "Sou5": {"small": small_Sou5_img, "small_right": small_right_Sou5_img, "small_up": small_up_Sou5_img, "small_left": small_left_Sou5_img}, "Sou6": {"small": small_Sou6_img, "small_right": small_right_Sou6_img, "small_up": small_up_Sou6_img, "small_left": small_left_Sou6_img}, "Sou7": {"small": small_Sou7_img, "small_right": small_right_Sou7_img, "small_up": small_up_Sou7_img, "small_left": small_left_Sou7_img}, "Sou8": {"small": small_Sou8_img, "small_right": small_right_Sou8_img, "small_up": small_up_Sou8_img, "small_left": small_left_Sou8_img}, "Sou9": {"small": small_Sou9_img, "small_right": small_right_Sou9_img, "small_up": small_up_Sou9_img, "small_left": small_left_Sou9_img}, "Ton": {"small": small_Ton_img, "small_right": small_right_Ton_img, "small_up": small_up_Ton_img, "small_left": small_left_Ton_img}, "Nan": {"small": small_Nan_img, "small_right": small_right_Nan_img, "small_up": small_up_Nan_img, "small_left": small_left_Nan_img}, "Shaa": {"small": small_Shaa_img, "small_right": small_right_Shaa_img, "small_up": small_up_Shaa_img, "small_left": small_left_Shaa_img}, "Pei": {"small": small_Pei_img, "small_right": small_right_Pei_img, "small_up": small_up_Pei_img, "small_left": small_left_Pei_img}, "Chun": {"small": small_Chun_img, "small_right": small_right_Chun_img, "small_up": small_up_Chun_img, "small_left": small_left_Chun_img}, "Haku": {"small": small_Haku_img, "small_right": small_right_Haku_img, "small_up": small_up_Haku_img, "small_left": small_left_Haku_img}, "Hatsu": {"small": small_Hatsu_img, "small_right": small_right_Hatsu_img, "small_up": small_up_Hatsu_img, "small_left": small_left_Hatsu_img}, "Man5_red": {"small": small_Man5_red_img, "small_right": small_right_Man5_red_img, "small_up": small_up_Man5_red_img, "small_left": small_left_Man5_red_img}, "Pin5_red": {"small": small_Pin5_red_img, "small_right": small_right_Pin5_red_img, "small_up": small_up_Pin5_red_img, "small_left": small_left_Pin5_red_img}, "Sou5_red": {"small": small_Sou5_red_img, "small_right": small_right_Sou5_red_img, "small_up": small_up_Sou5_red_img, "small_left": small_left_Sou5_red_img}}

        # 麻將排序
        self.MAHJONG_SORT_TABLE_LIST = ["Man1", "Man2", "Man3", "Man4", "Man5", "Man5_red", "Man6", "Man7", "Man8", "Man9", "Pin1", "Pin2", "Pin3", "Pin4", "Pin5", "Pin5_red", "Pin6",
                                        "Pin7", "Pin8", "Pin9", "Sou1", "Sou2", "Sou3", "Sou4", "Sou5", "Sou5_red", "Sou6", "Sou7", "Sou8", "Sou9", "Ton", "Nan", "Shaa", "Pei", "Chun", "Haku", "Hatsu"]

        # 手牌, 二維列表, [順位,Mahjong物件]
        self.HAND_CARDS_LIST = []
        self.RIGHT_HAND_CARDS_LIST = []
        self.UP_HAND_CARDS_LIST = []
        self.LEFT_HAND_CARDS_LIST = []

        # 連線全域變數
        self.BUFF_SIZE = 4096
        self.SERVER_IP = "127.0.0.1"
        self.PORT = 6666
        self.cSocket = 0

        # 多執行緒函式

        self.NO_DEAL = 0  # =1玩家不抽牌

        self.VICE_DEWS_SITE_CHI = ""
        self.VICE_DEWS_SITE_PONG_KONG = ""

        self.IS_PONGING_OR_KONGING = 0  # 給t_chi判斷是否有其他人可以碰槓
        self.IS_PONGED_OR_KONGED = 0  # 讓t_chi知道其他人最後是否有碰槓
        self.IS_CHIING = 0  # 讓t_pong_kong判斷SEED要不要直接加(沒有其他家能吃就可以直接加)


class Dora_Mountain:
    def __init__(self):
        self.kong_mountain = []
        # 表寶牌(id list)
        self.dora_cards = []
        # 裏寶牌(id list)
        self.inner_dora_cards = []
        # 目前寶牌翻出數量
        self.flip_out_num = 0
        self.next_flip_index = 0

    def dora_init(self, GV):
        # 抓槓牌四張
        i = 0
        while i < 4:
            self.kong_mountain.append(
                GV.CARD_MOUNTAIN[(len(GV.CARD_MOUNTAIN)-1)])
            del GV.CARD_MOUNTAIN[(len(GV.CARD_MOUNTAIN)-1)]
            i += 1
        # 抓寶牌十張
        i = 0
        while i < 5:
            self.dora_cards.append(GV.CARD_MOUNTAIN[(len(GV.CARD_MOUNTAIN)-1)])
            del GV.CARD_MOUNTAIN[(len(GV.CARD_MOUNTAIN)-1)]
            self.inner_dora_cards.append(
                GV.CARD_MOUNTAIN[(len(GV.CARD_MOUNTAIN)-1)])
            del GV.CARD_MOUNTAIN[(len(GV.CARD_MOUNTAIN)-1)]
            i += 1

    def deal(self, GV, site):  # 發牌, type="","draw"

        if site == "down":
            GV.player_list[0].deal_card = self.kong_mountain[0]

        if site == "right":
            GV.player_list[1].deal_card = self.kong_mountain[0]

        if site == "up":
            GV.player_list[2].deal_card = self.kong_mountain[0]

        if site == "left":
            GV.player_list[3].deal_card = self.kong_mountain[0]

        del self.kong_mountain[0]
        # 牌山-1張牌
        del GV.CARD_MOUNTAIN[(len(GV.CARD_MOUNTAIN)-1)]

        # 寶牌翻牌

    def flip_dora(self):  # 寶牌翻牌
        self.flip_out_num += 1
        # self.dora_cards[self.next_flip_index].to_front()
        self.next_flip_index += 1
        return self.dora_cards[self.next_flip_index-1]


with open(MEMBER_FILE) as fp:
    MEMBER = json.load(fp)
login_area_t = threading.Thread(target=login_area)
login_area_t.setDaemon(True)
login_area_t.start()

wait_main_send_client_t = threading.Thread(target=wait_main_send_client)
wait_main_send_client_t.setDaemon(True)
wait_main_send_client_t.start()

wait_main_recv_client_t = threading.Thread(target=wait_main_recv_client)
wait_main_recv_client_t.setDaemon(True)
wait_main_recv_client_t.start()

wait_sub_send_client_t = threading.Thread(target=wait_sub_send_client)
wait_sub_send_client_t.setDaemon(True)
wait_sub_send_client_t.start()

wait_sub_recv_client_t = threading.Thread(target=wait_sub_recv_client)
wait_sub_recv_client_t.setDaemon(True)
wait_sub_recv_client_t.start()

wait_main_send_client_t.join()
wait_main_recv_client_t.join()
wait_sub_send_client_t.join()
wait_sub_recv_client_t.join()
