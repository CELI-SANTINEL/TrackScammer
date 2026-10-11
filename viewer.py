# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "viewer.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("48156428e37b723b4650e167139930fc42cdc3a3612e41113e201c7cdbe28f871791382d0a34c3c06a3a9dea101c9fbfe640cbc45700368ca62867ce3d786015")
_K2 = bytes.fromhex("2cd4bbf133c148b6b9b623007f558d647c067e6621beaa933b912002d42f576ec26013634b97419b415d9abc17cd23ea5f66ac1857119b2362c483eb89541903")
_K3 = bytes.fromhex("8ab759a063503956b8b919c017b093719d6a1653cd4b6feff2c7272f55d368b8123c23c69bf69704136127e6bb80b649055db59b5ddbf5567bd780cf3933da87")
_S = """maH2f*rr&F+2HgT7Q7fOA~D;aY&sPG@jhd9ejQc-S?C|?NQ2Sh;1R>J3L@ocw5=S&^ZtuTOgb|_JApnu
D60=`<Y0B?75jSi-<oaH?gS-pE3J<fGaR@C?@SN$TBWlRq>U)JBAsghFP&EG#fKfZC^V;v5k!MB4mQ0+
n2TY`i)^mD&~Dwhzqn##C>i&KuliHTzq~GV2y7igl6@|Y5Bj_sO%oP9F-B`=A_^fH2g??cp>-L-6L!Y>
KPJY*k7c)7W&~2oLT_zg<}Km6>ksB+RA<)R461-@76;%>h?6zR2|!V=-{Wh(F;Y;XBWyr#T6b;6rn#)4
2!IV?RX<>ZVrho<_Q^mp3nMx{9OUw*K>jN?ou6i!O;O<2KGlEGE&3~=Y0y0<@>duVE^IO|>zr0UL{oMr
_ScBTN<d#l*OWct^bTnKUonHrhQrSKoDt!bg!kuq0A#gm)^l1Gzo6t$Wl_l$Eenu?vvkG#6>Bsa(j19i
?6GwDN5%`dF-^<ndep0o;zhlen7fnIc*Z1hYkrJETT}&u#7!KqVOTBs&M=4rUF$x&OK&EQPt;?D*I~eF
dt12aorS+Tyv4EX?Y*qt;kTp*;xUpmZ?}iZOQc<uN|if}$8k5<-a-+S$WJw*2+sziR?H>x<ETSY^<y%e
=aDE4vKAY($L+19>vw|TD8cL2n=x(`6JyJtbd=te3+@}O5`-s)?x2Z*T^W{8Ub09d#I7)EO~L~qcjyeO
%9TRCLY5+2#(_<(YI#=Srmpf93Kt@Z!ziR2sY?<Sk=VM#Kg2a`DhfUlwi%-Y$+g82T-23_lknHQdTx(3
z*ZpyGIpg~+p*r&p?+Kwv}r<|MZ(%mPyunHkO!sU^!+X`dsd_4iW)<z5jB8n?eUfB5d(I!c9Z(sV!b=o
pYE+1p!_l73cNr0;L`HnB-&`SV#_ZkTGo#1?j?<OrU`xpOzh#+X>`}v4>;|KjN%1-?gc%q*N9n(G*<!&
lrS-`8X!dt9CZ}Z>{H^G1gkxBHos6^?VNa9p(Rde60|$oYv!i$#BqK;zgvXkb+Ci(g;#wyD6*$3YTE*t
ym-IzEMtX*cFar`D~U4VhHmX_A`i(@u)*pmv6&fvcj5+To<(PhEan;lH~PFB>!$qar^p2K^_4k0JvAM7
0ywLq*q6HuZSWfe!on{cK6@7|V1kKEgm;zlV-WjLNsG-AXzM`<wmY+>dGCFOou0?wxO3r<&0z(T@ko!`
5WEwJ*^3;9ev3SlKv64;4E-W3F{-`%627KNp!)pnOS;8JgW@{x{<1t9Wbhs8#*at%be&GT5RL?{d1l_N
S5c(eo5-zc8{^P#mH;^n^}<5k^rS8wVec(Ab24jMdUjU2<nrsuz`jh0(M<EK1E?mel#6j%|J3>Vwt=OW
e-XQiO=`?Guw5s+t6kd1D^1CsW!M<i<C6T0qz+)z1^xr}Rf$QxUVd@j-qHST{o5op3O7dg*DU7xc;z6F
j+Q^tuf=n<K8M(LO0z7q`$1FqlFXFsQBC`_+0GJ+`12oxs@37(1_yMLLJ{%?Y&R=JgDT4TPYh+$fNz=8
J^}*UQu)%>$&4v<Vyzpc(voK~E=Ypa>K-SMDqd8^#whs%5e14*vhL=Hqnf#tCEs0SyhEu~&y<MR=S?kO
<?BX6bQs<K(YVKE`&;4~|6v%4+zQB=pHV9}yeWEo!8Gjvp!Jf$$Z{exT(C1TjGiUUF3RWsGoqS-5x|tT
9Dc)!TaN>ik-Sn*eYy!>?y_ut1#yLc7Rn90OT(B|89xBH6;tdQZi2_Qi@N{rAX}C*fWdU#e(I`Q;^cC;
#dNiu)(vV6j9pIH>WN?Yei66!DTjfigEe1f8PNb!uxH(ds;G^Eyz~UJiAn%%z2h`S-9=eNxZBz4`X65d
VvUElb4dcs$GFCMbPsA&zE!Mx=<5)(oc5VkVF)0B^X*KD%4O`e^gO`7bi$53{(RX;eY1>vmOLQx_XoE>
Tz$sOQ{{8nI7{9FYH21^Ph}(d%i)Yn)#)I+u=WieA!(`)qoil!BPcmefOV>m4+~k<lHj6S3cayx<wzg5
OWEBB-vCdrya+7dU>|Iw^b&amV8qXaT|jTPe!~eVEFk`e0Y=vLqVO!yVNlahTFzPQN@=SIS+C86C?E)D
ikkK_%$h)iWVWzHZPZY5eZR=W_o2r!(4X+LXC*|R-%{F_1cf3O!hqO(vg{!eNw2)GM(-t>T>>8TW|PP#
yDf4#-^`|P!68n#^|SIt`Ml@IHU#*ZkZEeeDMZq2u4?al?7aV~A0GDmNJ2#|&~iOsLo*?<ry4rV+vUBA
WgvV{nm4%ksMBY7W)Y`bl9RC*_yph%<Ok;mFT$$MPde2hlnn-APpAZpb&|u*2N$3PZ@v6baaN^*W>TNK
Dw;9FP{(pDNkPoDw)G8R{*#>f!Imq2064dX_CX3RGBec6>}YGDnfAzJIJN7dj<j@cf~?7aa*U2)cl>q5
zne_C3==&mVmJ(%(%P_5TLw{CX8z(QO_EVu7s1CxaTT68{SJpcO7Q+k$<}V-_2D>akrv8P0<c5wM8h#R
w0$+?|32Jy2?a=+4ATnKNCZF#!l#>-Q-~~d%_YUB>STi*0u0=!&VUa<bViz<gZ{Jn(>+KD8wBIgg~w2E
Q}UXHlD-beB%9O^8T7&1wuR+};(889OFnhUx=!EOUx?kLI~Kr035mp3G;x?;X=tViqto(NtOh_>$|vjf
VV<KHB@xS|leGSzD;Zbha`h;3D;=Cjh=^=p55h{G0ioP6g;RUaNx{uAvsM^k17=x1i=k#vK!ci;U|h&M
okDM+XK>Y5?3r`l$Vd45P-@ygGYE+;-%_JBDa<47=c=FaTKXOjvbsOcWTMZBJ7s&z6rq3fHRRn~!?El&
U;)iEj^#}U=*|&csHU%^;BfIx=Rn}VEJn{RGq!JKT^df_oj17X$eu6<cPCSb1|J!yhP030A|)?hF)=RQ
lB2XxhP6xJ;QP?9-i~E}K)O_IHG5~1j1Eb`kWd%op!+>?t-{L&g13|r4J@Or(c+lpi^Vh+W?52Fp3)ZK
eW|8%^lC^gV+2TSbg<c=3JqMn-~`XK3-HN|VyxB<a*FfXAm1S>SdH>c-f?+p9*2B!J7pFJ{qZx=D-YF?
5YO~Eb+5lW*>v3Py{T76rPR`xM<E%8VG){uQL3q;$Jdmp0ppYrFmW|k{2Am*aq?$q9D1&yxln>vz1zm@
@VnE~vq|{Rx7VpkEW8b)qSW2;rq4DM%k@D8b;ts;Qoiqkeiw_9wxen_+q+jL^?v%>DWA20&H@t}q~2NT
4;`J4OYoZ@twU5r(YK>+Dv?51^vEVLa0Oy$$Z^$aw0;30!dUM#9d(l%bBHQ37Rjs=JPAmdSBoc;E(&4I
qfZUiRatw2c8KNM18VJo50I=u@ZS#fXx`ahm~TX86}FPJQmkY}OEW|T6kz2%UT}L-jQ8?!5l!}LDDkGc
8{<38`nZy;y8FQi@`2arRp2K_2@hkrGzs750bp$2BC%!OA}>8GEwICz-vOj1dLz0ze9>*8>5$n1)+>>S
ziI0O=;8$n0<z~2cS!ZYnJs<W+KiJ>J^~=uvlsWKFQpgDC4%3i%x(RnKXN_*x8zWJ=>n?hSMo>Jx)ic?
@@ta%qpJDd9jj=D!8yL}zA|UtE?63h;j}kSV_0KicX)uf|JaoQD=Vh6f)0{`vx(s=-BeLF3=iO%ep2q-
jS8F1r`t{lTaet|^G_4S=My%f0_O|`#Y}+jry)p*>`hXDC`H9x^06>1U4Rz=965e}nmzbm_04;NEX*i*
4!3z-$hXa`<h}2Wt05{jDl3>iwNQW<t5%m`_13X_&x|F^ab;!SVh)n-rAP=tV@};rA8knoBS)=gjV>8B
=^|i$xr>501)t|@R<kO|RlcVl{h4L`pP?J<TAvIG`J4z{b}E$IUl$*6+fX|PUI4f2k;6jm&mLS)n?~Fb
aq-KY0{W7qABFGyEcy;1*yBe<)NRg2nZV`uxq*s5_Ij_jM(_Bg=yR9G!7iYxn+_7T*e@4Pa8`e58Ue1)
d`dVCS~iYl>OGKCpHmH3lyh!l*8bswoW$N7DU$S#haagXp}FtdjHw&#Zo;o8UeS$6m;?|EY|^iU<mHa|
@$IPKBCq@i5$2Bl1&>lCg7l{8TqZOqT@L2@i0|Jyyl+0?B+q-MEfeD}to!(vL@lQ(!FM%6+HjDDSSWqZ
5aDCpR$V++6ktn#8iyHt)=+>Su7uNb2soSs?I4|#$(YYWq^MI1hhq%sr>l*<RPJY%LWal+3D%=c=aUt#
D+VIX0T9(9|6CD0Xc&wFJw&)oN^J?_HZca$Rkh<x<e&3knG;v12|E#)jYh8Da`qVRa^e4n!+Ay%l7Pt|
e4HU+vT17X03-z%X^HBE6m8nXKgZ2>ocGGD9vio=<$=nSCW*vqSjRpfYVSGNKL%uZ<}8`g8jG33(-cY$
G<*AGHKkZ?&n+F7E6~(x1<LC=cURV~Cb{o>66YMrgP_A1TN~%>HX63@S0|}h2c{&Ak+6Pz+Pd3j8~Lxh
z*HPVz!u>O{K{k_Q)Yp7G&VF45Xw|zxBSbCD5bH46!6)vHC^jcY?|wx$K}%Hk^&dXU$$~evUP(T52Nrw
4?Eb3K`=nE)<SIjg{^7tzIv2p5rT*pG=0Yiq%>Uf@I&|qYSomQ$r<#h(vHdoT!gJBTGca+w+PvhaDqs{
5cMODCDgkmnW`fa?~(g`MP;EQBn~SCp+hNOz>)>@bNC}79Rb8uCL5|!P4F^;pfNDqWC%Fr$#>K_{QPNV
`uH&h9DIoQ|E?gm$6%S&nk4#AmP)WR37L<lP2+FC-<T<LC#w4egpv"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)
