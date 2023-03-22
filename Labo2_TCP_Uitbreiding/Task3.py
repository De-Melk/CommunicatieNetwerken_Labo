import matplotlib.pyplot as plt

# in Kbps
F = 10 * 10**6
us = 20 * 1000
dmin = 1000

def client_server(n):
    return max(n*F/us, F/dmin)

def peer_to_peer(n, u):
    return max(F/us, F/dmin, n*F/(us + sum(u)))

if __name__ == '__main__':
    N = [10, 100, 1000]
    u = [200, 600, 1000]
    cs = [client_server(n) for n in N]
    p2p = [peer_to_peer(N[i], [u[i]] * N[i]) for i in range(len(N))]

    plt.plot(N, cs, 'bo')
    plt.plot(N, cs, 'b', label='Client-Server')
    plt.plot(N, p2p, 'ro')
    plt.plot(N, p2p, 'r', label='P2P')
    plt.legend(loc='upper-left')
    plt.title('Minimum Distribution Time for Client-Server vs Peer-to-Peer')
    plt.xlabel('Number of Peers')
    plt.ylabel('Minimum Distribution Time (Kbps)')
    plt.show()