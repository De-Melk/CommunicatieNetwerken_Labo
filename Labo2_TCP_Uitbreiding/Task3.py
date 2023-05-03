import matplotlib.pyplot as plt

F = 15 * 1024 * 1024     #filesize  (Kbits)
us = 30 * 1024      #server upload rate     (Kbits/s)
dmin = 2 * 1024        #download rate of slowest peer   (Kbits/s)

def client_server(n):       #calculate distribution time client-server
    return max((n*F)/us, F/dmin)

def peer_to_peer(n, u):     #calculate distribution time p2p
    return max(F/us, F/dmin, (n*F)/(us + (u*n)))

if __name__ == '__main__':
    N = [10, 100, 1000]         #Number of peers
    u = [300, 700, 2048]        #upload rate op peers (kbps)
    cs = [client_server(n) for n in N]
    p2p_300 = [peer_to_peer(N[i], u[0]) for i in range(len(N))]
    p2p_700 = [peer_to_peer(N[i], u[1]) for i in range(len(N))]
    p2p_2048 = [peer_to_peer(N[i], u[2]) for i in range(len(N))]

    plt.plot(N, cs, color='b', marker='o', label='Client-Server')       #plot all times on graph
    plt.plot(N, p2p_300, color='r', marker='o', label='p2p_300Kbps')
    plt.plot(N, p2p_700, 'orange', label='p2p_700Kbps', marker='o', color='orange')
    plt.plot(N, p2p_2048, 'yellow', label='p2p_2Mbps', marker='o', color='yellow')
    #plt.plot(N, p2p_2048, 'o')
    plt.legend(loc='upper left')
    plt.title('Minimum Distribution Time for Client-Server vs Peer-to-Peer')
    plt.xlabel('Number of Peers')
    plt.ylabel('Minimum Distribution Time (Kbps)')
    plt.show()