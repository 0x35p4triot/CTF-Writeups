from Crypto.Util.number import getPrime, bytes_to_long

FLAG = open('flag.txt', 'rb').read().strip()

def mask_expr(expr):
    global e, n
    assert '**' not in expr, "My computer is weak, I can't handle this insane calculation"
    assert len(expr) <= 4, "Too long!"
    assert all([c in r'pq+-*/%' for c in expr]), "Don't try to break me"
    res = eval(expr)
    return str(pow(res, e, n))[::2], pow(res, e, n), p, q, n, e


if __name__ == '__main__':

    e = 3
    p, q = 1, 1
    while p == q:
        while (p-1) % e == 0:
            p = getPrime(513)
        while (q-1) % e == 0:
            q = getPrime(513)
    # print(f"{p = }", p.bit_length())
    # print(f"{q = }", q.bit_length())
    n = p * q
    # print(f"{pow(p, e, n) = }")
    # print(f"{n = }")
    m = bytes_to_long(FLAG)
    c = pow(m, e, n)
    print(f'{c = }')
    for _ in range(20):
        expr = input('Input your expression in terms of p, q and r: ')
        print(mask_expr(expr))

# vanluongkma@Desktop:/mnt/c/Users/dinhv/Documents/GitHub/CTF-Writeups/CyberSpaceCTF2024/Crypto-Mask-RSA$ python3 test_server.py 
# p = 25290488719424949433989032564362708855076149690593710998669169861233282194421397589375922975865818040316934066082551868655875597308801144197306870648146909 513
# q = 24766472487689127389779248049948637543777377864620177990257905686079142757163119525889071313724100965751848155004807050971340615101579190472644061145951113 513
# pow(p, e, n) = 287627152565852689379937350351612283647292162583659845673332684236762194177851721376515737034543122846448692513996837410824416582703578785549732613547715761508195931984835823293016713917216487316340316823217607452160311387259248591176780923871366537915878586041912322866342875544334588859723648231743776877133
# n = 626356193069850241095714430666797882761834354037291483886654036860221836671251841638463578359737190914757162420849474528846650079874078625978289176596617868273875322145600874926244542251323610808837860694245955675537296047908005697324988133667512181222313062877655710027850551903609314835996568001521756059717
# c = 74777606227461956889771614759108018225860449460616378216552369417296767205273338346791374528263030651040166096573892453226402987876892977873269105663723635661343236734596620651154246738986433226563951268258998755169764030666851201256359293124577009275941159245849910125751058589572484504006872372726098805777
# Input your expression in terms of p, q and r: p
# 27212682839330562867912869463364372917571755304412448953987184152058859363475658991885223173126836436227042631829451770281657188801132632754358573421476713
# Input your expression in terms of p, q and r: q
# 17442410603282892723618602187529515359711740833730260149510807165116647546271374480187023501331151730764109747634675242379762827312400467020803390714945500
# Input your expression in terms of p, q and r: -p
# 38200097575700115914411561323232249443010697435908638696567102347749448553492075730675563288317242953708423794668516427076463044785437657739775722179799854
# Input your expression in terms of p, q and r: -q
# 48070269701857885058725729608087015001779693906580906591923479334681651370686349351273762840192927650161365578753491045997358305375179722463221005987230077
# Input your expression in terms of p, q and r: -p-q
# 11767686861427213280803869235613733183208847591177467547946294281532791016210791359487439676976091223943313946933930274706600116473036189618962432455853254
# Input your expression in terms of p, q and r: -p+q
# 56743418179093017738039163501752755702722348268738999836087009412866085109763450210862586890748303684462622542293181770456225972098837115859589113994745354
# Input your expression in terms of p, q and r: p+q
# 45755003543623364580520461651893888277383596238243719093508981227175406809747922372073256785557097167082251389554136923661410016114533190874162964246322313
# Input your expression in terms of p, q and r: p%q
# 10770261236047660043304167275744866658769005560682277804466276087931202717194273511698209562785775606462942883194885528811895260599732174633545282707430213
# Input your expression in terms of p, q and r: p//q
# 1
# Input your expression in terms of p, q and r: p*q
# 0
# Input your expression in terms of p, q and r: -p*q
# 0