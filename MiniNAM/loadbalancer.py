from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        # Inisiasi topologi
        Topo.__init__(self)

        # Add host dan switch
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')

        s1 = self.addSwitch('s1')

        # Add link
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s1, h3)
        self.addLink(s1, h4)
        self.addLink(s1, h5)
        self.addLink(s1, h6)
        self.addLink(s1, h7)
        self.addLink(s1, h8)
        self.addLink(s1, h9)
        self.addLink(s1, h10)


topos = {'mytopo': (lambda : MyTopo())}
locations = {'c0': (622,102), 'h1': (862,102), 'h8': (307,356), 'h6': (231,97), 'h9': (314,497), 'h5': (321,95), 'h10': (136,97), 'h7': (307,275), 'h3': (865,385), 'h2': (866,258), 'h4': (415,96), 's1': (621,258)}
