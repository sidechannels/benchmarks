#!/usr/bin/env python
#
# File isw_and_2s_rand.py
# 
# Copyright (C) 2019-2020, LIP6, Sorbonne Universite
# Written by Quentin L. Meunier
#
# This file is part of SELA
# 
# SELA is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
# 
# SELA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for
# more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with SELA. If not, see <https://www.gnu.org/licenses/>.
from leakage_verif import *

nbExps = 0
nbLeak = 0



firstOrder = True
secondOrder = False

def checkExpLeakageFirstOrder(e0):
    global nbExps
    global nbLeak
    #print('# checkExpLeakage: %s' % e0)
    res, usedBitExp, tpsTime = checkTpsVal(e0)
    nbExps += 1
    if not res:
        nbLeak += 1

    if not res:
        print('# Leakage exp num %d' % (nbExps))


def checkExpLeakageSecondOrder(e0, e1):
    global nbExps
    global nbLeak
    #print('# checkExpLeakage: (%s, %s)' % (e0, e1))
    res, usedBitExp, tpsTime = checkTpsTrans(e0, e1)
    nbExps += 1
    if not res:
        nbLeak += 1

    if not res:
        print('# Leakage for exp num %d' % (nbExps))



def uma1(k0, k1, k2, k3, k4, k5, k6, k7):
    global nbExps
    global nbLeak

    r_1720 = symbol('r_1720', 'M', 1)
    r_1721 = symbol('r_1721', 'M', 1)
    r_1722 = symbol('r_1722', 'M', 1)
    r_1723 = symbol('r_1723', 'M', 1)
    r_1724 = symbol('r_1724', 'M', 1)
    r_1725 = symbol('r_1725', 'M', 1)
    r_1726 = symbol('r_1726', 'M', 1)
    r_1727 = symbol('r_1727', 'M', 1)
    r_1728 = symbol('r_1728', 'M', 1)
    r_1729 = symbol('r_1729', 'M', 1)
    r_17210 = symbol('r_17210', 'M', 1)
    r_17211 = symbol('r_17211', 'M', 1)
    r_17212 = symbol('r_17212', 'M', 1)
    r_17213 = symbol('r_17213', 'M', 1)
    r_17214 = symbol('r_17214', 'M', 1)
    r_17215 = symbol('r_17215', 'M', 1)
    r0_72_17516 = symbol('r0_72_17516', 'M', 1)
    r1_72_17517 = symbol('r1_72_17517', 'M', 1)
    r2_72_17518 = symbol('r2_72_17518', 'M', 1)
    r0_73_17519 = symbol('r0_73_17519', 'M', 1)
    r1_73_17520 = symbol('r1_73_17520', 'M', 1)
    r2_73_17521 = symbol('r2_73_17521', 'M', 1)
    r0_74_17522 = symbol('r0_74_17522', 'M', 1)
    r1_74_17523 = symbol('r1_74_17523', 'M', 1)
    r2_74_17524 = symbol('r2_74_17524', 'M', 1)
    r0_75_17525 = symbol('r0_75_17525', 'M', 1)
    r1_75_17526 = symbol('r1_75_17526', 'M', 1)
    r2_75_17527 = symbol('r2_75_17527', 'M', 1)
    r0_76_17528 = symbol('r0_76_17528', 'M', 1)
    r1_76_17529 = symbol('r1_76_17529', 'M', 1)
    r2_76_17530 = symbol('r2_76_17530', 'M', 1)
    r0_77_17531 = symbol('r0_77_17531', 'M', 1)
    r1_77_17532 = symbol('r1_77_17532', 'M', 1)
    r2_77_17533 = symbol('r2_77_17533', 'M', 1)
    r0_78_17534 = symbol('r0_78_17534', 'M', 1)
    r1_78_17535 = symbol('r1_78_17535', 'M', 1)
    r2_78_17536 = symbol('r2_78_17536', 'M', 1)
    r0_79_17537 = symbol('r0_79_17537', 'M', 1)
    r1_79_17538 = symbol('r1_79_17538', 'M', 1)
    r2_79_17539 = symbol('r2_79_17539', 'M', 1)
    r0_89_17540 = symbol('r0_89_17540', 'M', 1)
    r1_89_17541 = symbol('r1_89_17541', 'M', 1)
    r2_89_17542 = symbol('r2_89_17542', 'M', 1)
    r0_90_17543 = symbol('r0_90_17543', 'M', 1)
    r1_90_17544 = symbol('r1_90_17544', 'M', 1)
    r2_90_17545 = symbol('r2_90_17545', 'M', 1)
    r0_100_17546 = symbol('r0_100_17546', 'M', 1)
    r1_100_17547 = symbol('r1_100_17547', 'M', 1)
    r2_100_17548 = symbol('r2_100_17548', 'M', 1)
    r0_101_17549 = symbol('r0_101_17549', 'M', 1)
    r1_101_17550 = symbol('r1_101_17550', 'M', 1)
    r2_101_17551 = symbol('r2_101_17551', 'M', 1)
    r0_107_17552 = symbol('r0_107_17552', 'M', 1)
    r1_107_17553 = symbol('r1_107_17553', 'M', 1)
    r2_107_17554 = symbol('r2_107_17554', 'M', 1)
    r0_108_17555 = symbol('r0_108_17555', 'M', 1)
    r1_108_17556 = symbol('r1_108_17556', 'M', 1)
    r2_108_17557 = symbol('r2_108_17557', 'M', 1)
    r0_111_17558 = symbol('r0_111_17558', 'M', 1)
    r1_111_17559 = symbol('r1_111_17559', 'M', 1)
    r2_111_17560 = symbol('r2_111_17560', 'M', 1)
    r0_112_17561 = symbol('r0_112_17561', 'M', 1)
    r1_112_17562 = symbol('r1_112_17562', 'M', 1)
    r2_112_17563 = symbol('r2_112_17563', 'M', 1)
    r0_118_17564 = symbol('r0_118_17564', 'M', 1)
    r1_118_17565 = symbol('r1_118_17565', 'M', 1)
    r2_118_17566 = symbol('r2_118_17566', 'M', 1)
    r0_119_17567 = symbol('r0_119_17567', 'M', 1)
    r1_119_17568 = symbol('r1_119_17568', 'M', 1)
    r2_119_17569 = symbol('r2_119_17569', 'M', 1)
    r0_120_17570 = symbol('r0_120_17570', 'M', 1)
    r1_120_17571 = symbol('r1_120_17571', 'M', 1)
    r2_120_17572 = symbol('r2_120_17572', 'M', 1)
    r0_121_17573 = symbol('r0_121_17573', 'M', 1)
    r1_121_17574 = symbol('r1_121_17574', 'M', 1)
    r2_121_17575 = symbol('r2_121_17575', 'M', 1)
    r0_122_17576 = symbol('r0_122_17576', 'M', 1)
    r1_122_17577 = symbol('r1_122_17577', 'M', 1)
    r2_122_17578 = symbol('r2_122_17578', 'M', 1)
    r0_123_17579 = symbol('r0_123_17579', 'M', 1)
    r1_123_17580 = symbol('r1_123_17580', 'M', 1)
    r2_123_17581 = symbol('r2_123_17581', 'M', 1)
    r0_124_17582 = symbol('r0_124_17582', 'M', 1)
    r1_124_17583 = symbol('r1_124_17583', 'M', 1)
    r2_124_17584 = symbol('r2_124_17584', 'M', 1)
    r0_125_17585 = symbol('r0_125_17585', 'M', 1)
    r1_125_17586 = symbol('r1_125_17586', 'M', 1)
    r2_125_17587 = symbol('r2_125_17587', 'M', 1)
    r0_126_17588 = symbol('r0_126_17588', 'M', 1)
    r1_126_17589 = symbol('r1_126_17589', 'M', 1)
    r2_126_17590 = symbol('r2_126_17590', 'M', 1)
    r0_127_17591 = symbol('r0_127_17591', 'M', 1)
    r1_127_17592 = symbol('r1_127_17592', 'M', 1)
    r2_127_17593 = symbol('r2_127_17593', 'M', 1)
    r0_128_17594 = symbol('r0_128_17594', 'M', 1)
    r1_128_17595 = symbol('r1_128_17595', 'M', 1)
    r2_128_17596 = symbol('r2_128_17596', 'M', 1)
    r0_129_17597 = symbol('r0_129_17597', 'M', 1)
    r1_129_17598 = symbol('r1_129_17598', 'M', 1)
    r2_129_17599 = symbol('r2_129_17599', 'M', 1)
    r0_130_175100 = symbol('r0_130_175100', 'M', 1)
    r1_130_175101 = symbol('r1_130_175101', 'M', 1)
    r2_130_175102 = symbol('r2_130_175102', 'M', 1)
    r0_131_175103 = symbol('r0_131_175103', 'M', 1)
    r1_131_175104 = symbol('r1_131_175104', 'M', 1)
    r2_131_175105 = symbol('r2_131_175105', 'M', 1)
    r0_132_175106 = symbol('r0_132_175106', 'M', 1)
    r1_132_175107 = symbol('r1_132_175107', 'M', 1)
    r2_132_175108 = symbol('r2_132_175108', 'M', 1)
    r0_133_175109 = symbol('r0_133_175109', 'M', 1)
    r1_133_175110 = symbol('r1_133_175110', 'M', 1)
    r2_133_175111 = symbol('r2_133_175111', 'M', 1)

    signals = []
    presharing0 = k0 ^ r_1720;

    presharing0 = simplify(presharing0)
    signals.append(presharing0)
    t1 = presharing0 ^ r_1721;

    t1 = simplify(t1)
    signals.append(t1)
    presharing2 = k1 ^ r_1722;

    presharing2 = simplify(presharing2)
    signals.append(presharing2)
    t3 = presharing2 ^ r_1723;

    t3 = simplify(t3)
    signals.append(t3)
    presharing4 = k2 ^ r_1724;

    presharing4 = simplify(presharing4)
    signals.append(presharing4)
    t5 = presharing4 ^ r_1725;

    t5 = simplify(t5)
    signals.append(t5)
    presharing6 = k3 ^ r_1726;

    presharing6 = simplify(presharing6)
    signals.append(presharing6)
    t7 = presharing6 ^ r_1727;

    t7 = simplify(t7)
    signals.append(t7)
    presharing8 = k4 ^ r_1728;

    presharing8 = simplify(presharing8)
    signals.append(presharing8)
    t9 = presharing8 ^ r_1729;

    t9 = simplify(t9)
    signals.append(t9)
    presharing10 = k5 ^ r_17210;

    presharing10 = simplify(presharing10)
    signals.append(presharing10)
    t11 = presharing10 ^ r_17211;

    t11 = simplify(t11)
    signals.append(t11)
    presharing12 = k6 ^ r_17212;

    presharing12 = simplify(presharing12)
    signals.append(presharing12)
    t13 = presharing12 ^ r_17213;

    t13 = simplify(t13)
    signals.append(t13)
    presharing14 = k7 ^ r_17214;

    presharing14 = simplify(presharing14)
    signals.append(presharing14)
    t15 = presharing14 ^ r_17215;

    t15 = simplify(t15)
    signals.append(t15)
    t16 = r_1726 ^ r_17210;

    t16 = simplify(t16)
    signals.append(t16)
    t17 = r_1727 ^ r_17211;

    t17 = simplify(t17)
    signals.append(t17)
    t18 = t7 ^ t11;

    t18 = simplify(t18)
    signals.append(t18)
    t19 = r_1720 ^ r_17212;

    t19 = simplify(t19)
    signals.append(t19)
    t20 = r_1721 ^ r_17213;

    t20 = simplify(t20)
    signals.append(t20)
    t21 = t1 ^ t13;

    t21 = simplify(t21)
    signals.append(t21)
    t22 = t19 ^ t16;

    t22 = simplify(t22)
    signals.append(t22)
    t23 = t20 ^ t17;

    t23 = simplify(t23)
    signals.append(t23)
    t24 = t21 ^ t18;

    t24 = simplify(t24)
    signals.append(t24)
    t25 = r_1720 ^ r_1726;

    t25 = simplify(t25)
    signals.append(t25)
    t26 = r_1721 ^ r_1727;

    t26 = simplify(t26)
    signals.append(t26)
    t27 = t1 ^ t7;

    t27 = simplify(t27)
    signals.append(t27)
    t28 = r_1720 ^ r_17210;

    t28 = simplify(t28)
    signals.append(t28)
    t29 = r_1721 ^ r_17211;

    t29 = simplify(t29)
    signals.append(t29)
    t30 = t1 ^ t11;

    t30 = simplify(t30)
    signals.append(t30)
    t31 = r_1722 ^ r_1724;

    t31 = simplify(t31)
    signals.append(t31)
    t32 = r_1723 ^ r_1725;

    t32 = simplify(t32)
    signals.append(t32)
    t33 = t3 ^ t5;

    t33 = simplify(t33)
    signals.append(t33)
    t34 = t31 ^ r_17214;

    t34 = simplify(t34)
    signals.append(t34)
    t35 = t32 ^ r_17215;

    t35 = simplify(t35)
    signals.append(t35)
    t36 = t33 ^ t15;

    t36 = simplify(t36)
    signals.append(t36)
    t37 = t34 ^ r_1726;

    t37 = simplify(t37)
    signals.append(t37)
    t38 = t35 ^ r_1727;

    t38 = simplify(t38)
    signals.append(t38)
    t39 = t36 ^ t7;

    t39 = simplify(t39)
    signals.append(t39)
    t40 = t34 ^ r_1720;

    t40 = simplify(t40)
    signals.append(t40)
    t41 = t35 ^ r_1721;

    t41 = simplify(t41)
    signals.append(t41)
    t42 = t36 ^ t1;

    t42 = simplify(t42)
    signals.append(t42)
    t43 = t34 ^ r_17212;

    t43 = simplify(t43)
    signals.append(t43)
    t44 = t35 ^ r_17213;

    t44 = simplify(t44)
    signals.append(t44)
    t45 = t36 ^ t13;

    t45 = simplify(t45)
    signals.append(t45)
    t46 = r_1728 ^ t22;

    t46 = simplify(t46)
    signals.append(t46)
    t47 = r_1729 ^ t23;

    t47 = simplify(t47)
    signals.append(t47)
    t48 = t9 ^ t24;

    t48 = simplify(t48)
    signals.append(t48)
    t49 = t43 ^ t28;

    t49 = simplify(t49)
    signals.append(t49)
    t50 = t44 ^ t29;

    t50 = simplify(t50)
    signals.append(t50)
    t51 = t45 ^ t30;

    t51 = simplify(t51)
    signals.append(t51)
    t52 = t46 ^ r_17210;

    t52 = simplify(t52)
    signals.append(t52)
    t53 = t47 ^ r_17211;

    t53 = simplify(t53)
    signals.append(t53)
    t54 = t48 ^ t11;

    t54 = simplify(t54)
    signals.append(t54)
    t55 = t46 ^ r_1722;

    t55 = simplify(t55)
    signals.append(t55)
    t56 = t47 ^ r_1723;

    t56 = simplify(t56)
    signals.append(t56)
    t57 = t48 ^ t3;

    t57 = simplify(t57)
    signals.append(t57)
    t58 = t52 ^ r_17214;

    t58 = simplify(t58)
    signals.append(t58)
    t59 = t53 ^ r_17215;

    t59 = simplify(t59)
    signals.append(t59)
    t60 = t54 ^ t15;

    t60 = simplify(t60)
    signals.append(t60)
    t61 = t52 ^ t31;

    t61 = simplify(t61)
    signals.append(t61)
    t62 = t53 ^ t32;

    t62 = simplify(t62)
    signals.append(t62)
    t63 = t54 ^ t33;

    t63 = simplify(t63)
    signals.append(t63)
    t64 = t55 ^ t25;

    t64 = simplify(t64)
    signals.append(t64)
    t65 = t56 ^ t26;

    t65 = simplify(t65)
    signals.append(t65)
    t66 = t57 ^ t27;

    t66 = simplify(t66)
    signals.append(t66)
    t67 = r_17214 ^ t64;

    t67 = simplify(t67)
    signals.append(t67)
    t68 = r_17215 ^ t65;

    t68 = simplify(t68)
    signals.append(t68)
    t69 = t15 ^ t66;

    t69 = simplify(t69)
    signals.append(t69)
    t70 = t61 ^ t64;

    t70 = simplify(t70)
    signals.append(t70)
    t71 = t62 ^ t65;

    t71 = simplify(t71)
    signals.append(t71)
    t72 = t63 ^ t66;

    t72 = simplify(t72)
    signals.append(t72)
    t73 = t61 ^ t28;

    t73 = simplify(t73)
    signals.append(t73)
    t74 = t62 ^ t29;

    t74 = simplify(t74)
    signals.append(t74)
    t75 = t63 ^ t30;

    t75 = simplify(t75)
    signals.append(t75)
    t76 = t31 ^ t64;

    t76 = simplify(t76)
    signals.append(t76)
    t77 = t32 ^ t65;

    t77 = simplify(t77)
    signals.append(t77)
    t78 = t33 ^ t66;

    t78 = simplify(t78)
    signals.append(t78)
    t79 = t19 ^ t76;

    t79 = simplify(t79)
    signals.append(t79)
    t80 = t20 ^ t77;

    t80 = simplify(t80)
    signals.append(t80)
    t81 = t21 ^ t78;

    t81 = simplify(t81)
    signals.append(t81)
    t82 = r_1720 ^ t76;

    t82 = simplify(t82)
    signals.append(t82)
    t83 = r_1721 ^ t77;

    t83 = simplify(t83)
    signals.append(t83)
    t84 = t1 ^ t78;

    t84 = simplify(t84)
    signals.append(t84)
    t85 = t22 & t52;

    t85 = simplify(t85)
    signals.append(t85)
    t86 = t23 & t53;

    t86 = simplify(t86)
    signals.append(t86)
    t87 = t24 & t54;

    t87 = simplify(t87)
    signals.append(t87)
    t88 = t22 & t54;

    t88 = simplify(t88)
    signals.append(t88)
    t89 = t23 & t52;

    t89 = simplify(t89)
    signals.append(t89)
    t90 = t24 & t53;

    t90 = simplify(t90)
    signals.append(t90)
    t91 = t24 & t52;

    t91 = simplify(t91)
    signals.append(t91)
    t92 = t22 & t53;

    t92 = simplify(t92)
    signals.append(t92)
    t93 = t23 & t54;

    t93 = simplify(t93)
    signals.append(t93)
    t94 = t85 ^ r0_72_17516;

    t94 = simplify(t94)
    signals.append(t94)
    t95 = t94 ^ t88;

    t95 = simplify(t95)
    signals.append(t95)
    t96 = t95 ^ t91;

    t96 = simplify(t96)
    signals.append(t96)
    t97 = t96 ^ r2_72_17518;

    t97 = simplify(t97)
    signals.append(t97)
    t98 = t86 ^ r1_72_17517;

    t98 = simplify(t98)
    signals.append(t98)
    t99 = t98 ^ t89;

    t99 = simplify(t99)
    signals.append(t99)
    t100 = t99 ^ t92;

    t100 = simplify(t100)
    signals.append(t100)
    t101 = t100 ^ r0_72_17516;

    t101 = simplify(t101)
    signals.append(t101)
    t102 = t87 ^ r2_72_17518;

    t102 = simplify(t102)
    signals.append(t102)
    t103 = t102 ^ t90;

    t103 = simplify(t103)
    signals.append(t103)
    t104 = t103 ^ t93;

    t104 = simplify(t104)
    signals.append(t104)
    t105 = t104 ^ r1_72_17517;

    t105 = simplify(t105)
    signals.append(t105)
    t106 = t49 & t58;

    t106 = simplify(t106)
    signals.append(t106)
    t107 = t50 & t59;

    t107 = simplify(t107)
    signals.append(t107)
    t108 = t51 & t60;

    t108 = simplify(t108)
    signals.append(t108)
    t109 = t49 & t60;

    t109 = simplify(t109)
    signals.append(t109)
    t110 = t50 & t58;

    t110 = simplify(t110)
    signals.append(t110)
    t111 = t51 & t59;

    t111 = simplify(t111)
    signals.append(t111)
    t112 = t51 & t58;

    t112 = simplify(t112)
    signals.append(t112)
    t113 = t49 & t59;

    t113 = simplify(t113)
    signals.append(t113)
    t114 = t50 & t60;

    t114 = simplify(t114)
    signals.append(t114)
    t115 = t106 ^ r0_73_17519;

    t115 = simplify(t115)
    signals.append(t115)
    t116 = t115 ^ t109;

    t116 = simplify(t116)
    signals.append(t116)
    t117 = t116 ^ t112;

    t117 = simplify(t117)
    signals.append(t117)
    t118 = t117 ^ r2_73_17521;

    t118 = simplify(t118)
    signals.append(t118)
    t119 = t107 ^ r1_73_17520;

    t119 = simplify(t119)
    signals.append(t119)
    t120 = t119 ^ t110;

    t120 = simplify(t120)
    signals.append(t120)
    t121 = t120 ^ t113;

    t121 = simplify(t121)
    signals.append(t121)
    t122 = t121 ^ r0_73_17519;

    t122 = simplify(t122)
    signals.append(t122)
    t123 = t108 ^ r2_73_17521;

    t123 = simplify(t123)
    signals.append(t123)
    t124 = t123 ^ t111;

    t124 = simplify(t124)
    signals.append(t124)
    t125 = t124 ^ t114;

    t125 = simplify(t125)
    signals.append(t125)
    t126 = t125 ^ r1_73_17520;

    t126 = simplify(t126)
    signals.append(t126)
    t127 = t37 & r_17214;

    t127 = simplify(t127)
    signals.append(t127)
    t128 = t38 & r_17215;

    t128 = simplify(t128)
    signals.append(t128)
    t129 = t39 & t15;

    t129 = simplify(t129)
    signals.append(t129)
    t130 = t37 & t15;

    t130 = simplify(t130)
    signals.append(t130)
    t131 = t38 & r_17214;

    t131 = simplify(t131)
    signals.append(t131)
    t132 = t39 & r_17215;

    t132 = simplify(t132)
    signals.append(t132)
    t133 = t39 & r_17214;

    t133 = simplify(t133)
    signals.append(t133)
    t134 = t37 & r_17215;

    t134 = simplify(t134)
    signals.append(t134)
    t135 = t38 & t15;

    t135 = simplify(t135)
    signals.append(t135)
    t136 = t127 ^ r0_74_17522;

    t136 = simplify(t136)
    signals.append(t136)
    t137 = t136 ^ t130;

    t137 = simplify(t137)
    signals.append(t137)
    t138 = t137 ^ t133;

    t138 = simplify(t138)
    signals.append(t138)
    t139 = t138 ^ r2_74_17524;

    t139 = simplify(t139)
    signals.append(t139)
    t140 = t128 ^ r1_74_17523;

    t140 = simplify(t140)
    signals.append(t140)
    t141 = t140 ^ t131;

    t141 = simplify(t141)
    signals.append(t141)
    t142 = t141 ^ t134;

    t142 = simplify(t142)
    signals.append(t142)
    t143 = t142 ^ r0_74_17522;

    t143 = simplify(t143)
    signals.append(t143)
    t144 = t129 ^ r2_74_17524;

    t144 = simplify(t144)
    signals.append(t144)
    t145 = t144 ^ t132;

    t145 = simplify(t145)
    signals.append(t145)
    t146 = t145 ^ t135;

    t146 = simplify(t146)
    signals.append(t146)
    t147 = t146 ^ r1_74_17523;

    t147 = simplify(t147)
    signals.append(t147)
    t148 = t19 & t76;

    t148 = simplify(t148)
    signals.append(t148)
    t149 = t20 & t77;

    t149 = simplify(t149)
    signals.append(t149)
    t150 = t21 & t78;

    t150 = simplify(t150)
    signals.append(t150)
    t151 = t19 & t78;

    t151 = simplify(t151)
    signals.append(t151)
    t152 = t20 & t76;

    t152 = simplify(t152)
    signals.append(t152)
    t153 = t21 & t77;

    t153 = simplify(t153)
    signals.append(t153)
    t154 = t21 & t76;

    t154 = simplify(t154)
    signals.append(t154)
    t155 = t19 & t77;

    t155 = simplify(t155)
    signals.append(t155)
    t156 = t20 & t78;

    t156 = simplify(t156)
    signals.append(t156)
    t157 = t148 ^ r0_75_17525;

    t157 = simplify(t157)
    signals.append(t157)
    t158 = t157 ^ t151;

    t158 = simplify(t158)
    signals.append(t158)
    t159 = t158 ^ t154;

    t159 = simplify(t159)
    signals.append(t159)
    t160 = t159 ^ r2_75_17527;

    t160 = simplify(t160)
    signals.append(t160)
    t161 = t149 ^ r1_75_17526;

    t161 = simplify(t161)
    signals.append(t161)
    t162 = t161 ^ t152;

    t162 = simplify(t162)
    signals.append(t162)
    t163 = t162 ^ t155;

    t163 = simplify(t163)
    signals.append(t163)
    t164 = t163 ^ r0_75_17525;

    t164 = simplify(t164)
    signals.append(t164)
    t165 = t150 ^ r2_75_17527;

    t165 = simplify(t165)
    signals.append(t165)
    t166 = t165 ^ t153;

    t166 = simplify(t166)
    signals.append(t166)
    t167 = t166 ^ t156;

    t167 = simplify(t167)
    signals.append(t167)
    t168 = t167 ^ r1_75_17526;

    t168 = simplify(t168)
    signals.append(t168)
    t169 = t43 & t34;

    t169 = simplify(t169)
    signals.append(t169)
    t170 = t44 & t35;

    t170 = simplify(t170)
    signals.append(t170)
    t171 = t45 & t36;

    t171 = simplify(t171)
    signals.append(t171)
    t172 = t43 & t36;

    t172 = simplify(t172)
    signals.append(t172)
    t173 = t44 & t34;

    t173 = simplify(t173)
    signals.append(t173)
    t174 = t45 & t35;

    t174 = simplify(t174)
    signals.append(t174)
    t175 = t45 & t34;

    t175 = simplify(t175)
    signals.append(t175)
    t176 = t43 & t35;

    t176 = simplify(t176)
    signals.append(t176)
    t177 = t44 & t36;

    t177 = simplify(t177)
    signals.append(t177)
    t178 = t169 ^ r0_76_17528;

    t178 = simplify(t178)
    signals.append(t178)
    t179 = t178 ^ t172;

    t179 = simplify(t179)
    signals.append(t179)
    t180 = t179 ^ t175;

    t180 = simplify(t180)
    signals.append(t180)
    t181 = t180 ^ r2_76_17530;

    t181 = simplify(t181)
    signals.append(t181)
    t182 = t170 ^ r1_76_17529;

    t182 = simplify(t182)
    signals.append(t182)
    t183 = t182 ^ t173;

    t183 = simplify(t183)
    signals.append(t183)
    t184 = t183 ^ t176;

    t184 = simplify(t184)
    signals.append(t184)
    t185 = t184 ^ r0_76_17528;

    t185 = simplify(t185)
    signals.append(t185)
    t186 = t171 ^ r2_76_17530;

    t186 = simplify(t186)
    signals.append(t186)
    t187 = t186 ^ t174;

    t187 = simplify(t187)
    signals.append(t187)
    t188 = t187 ^ t177;

    t188 = simplify(t188)
    signals.append(t188)
    t189 = t188 ^ r1_76_17529;

    t189 = simplify(t189)
    signals.append(t189)
    t190 = t40 & t67;

    t190 = simplify(t190)
    signals.append(t190)
    t191 = t41 & t68;

    t191 = simplify(t191)
    signals.append(t191)
    t192 = t42 & t69;

    t192 = simplify(t192)
    signals.append(t192)
    t193 = t40 & t69;

    t193 = simplify(t193)
    signals.append(t193)
    t194 = t41 & t67;

    t194 = simplify(t194)
    signals.append(t194)
    t195 = t42 & t68;

    t195 = simplify(t195)
    signals.append(t195)
    t196 = t42 & t67;

    t196 = simplify(t196)
    signals.append(t196)
    t197 = t40 & t68;

    t197 = simplify(t197)
    signals.append(t197)
    t198 = t41 & t69;

    t198 = simplify(t198)
    signals.append(t198)
    t199 = t190 ^ r0_77_17531;

    t199 = simplify(t199)
    signals.append(t199)
    t200 = t199 ^ t193;

    t200 = simplify(t200)
    signals.append(t200)
    t201 = t200 ^ t196;

    t201 = simplify(t201)
    signals.append(t201)
    t202 = t201 ^ r2_77_17533;

    t202 = simplify(t202)
    signals.append(t202)
    t203 = t191 ^ r1_77_17532;

    t203 = simplify(t203)
    signals.append(t203)
    t204 = t203 ^ t194;

    t204 = simplify(t204)
    signals.append(t204)
    t205 = t204 ^ t197;

    t205 = simplify(t205)
    signals.append(t205)
    t206 = t205 ^ r0_77_17531;

    t206 = simplify(t206)
    signals.append(t206)
    t207 = t192 ^ r2_77_17533;

    t207 = simplify(t207)
    signals.append(t207)
    t208 = t207 ^ t195;

    t208 = simplify(t208)
    signals.append(t208)
    t209 = t208 ^ t198;

    t209 = simplify(t209)
    signals.append(t209)
    t210 = t209 ^ r1_77_17532;

    t210 = simplify(t210)
    signals.append(t210)
    t211 = t25 & t64;

    t211 = simplify(t211)
    signals.append(t211)
    t212 = t26 & t65;

    t212 = simplify(t212)
    signals.append(t212)
    t213 = t27 & t66;

    t213 = simplify(t213)
    signals.append(t213)
    t214 = t25 & t66;

    t214 = simplify(t214)
    signals.append(t214)
    t215 = t26 & t64;

    t215 = simplify(t215)
    signals.append(t215)
    t216 = t27 & t65;

    t216 = simplify(t216)
    signals.append(t216)
    t217 = t27 & t64;

    t217 = simplify(t217)
    signals.append(t217)
    t218 = t25 & t65;

    t218 = simplify(t218)
    signals.append(t218)
    t219 = t26 & t66;

    t219 = simplify(t219)
    signals.append(t219)
    t220 = t211 ^ r0_78_17534;

    t220 = simplify(t220)
    signals.append(t220)
    t221 = t220 ^ t214;

    t221 = simplify(t221)
    signals.append(t221)
    t222 = t221 ^ t217;

    t222 = simplify(t222)
    signals.append(t222)
    t223 = t222 ^ r2_78_17536;

    t223 = simplify(t223)
    signals.append(t223)
    t224 = t212 ^ r1_78_17535;

    t224 = simplify(t224)
    signals.append(t224)
    t225 = t224 ^ t215;

    t225 = simplify(t225)
    signals.append(t225)
    t226 = t225 ^ t218;

    t226 = simplify(t226)
    signals.append(t226)
    t227 = t226 ^ r0_78_17534;

    t227 = simplify(t227)
    signals.append(t227)
    t228 = t213 ^ r2_78_17536;

    t228 = simplify(t228)
    signals.append(t228)
    t229 = t228 ^ t216;

    t229 = simplify(t229)
    signals.append(t229)
    t230 = t229 ^ t219;

    t230 = simplify(t230)
    signals.append(t230)
    t231 = t230 ^ r1_78_17535;

    t231 = simplify(t231)
    signals.append(t231)
    t232 = t16 & t70;

    t232 = simplify(t232)
    signals.append(t232)
    t233 = t17 & t71;

    t233 = simplify(t233)
    signals.append(t233)
    t234 = t18 & t72;

    t234 = simplify(t234)
    signals.append(t234)
    t235 = t16 & t72;

    t235 = simplify(t235)
    signals.append(t235)
    t236 = t17 & t70;

    t236 = simplify(t236)
    signals.append(t236)
    t237 = t18 & t71;

    t237 = simplify(t237)
    signals.append(t237)
    t238 = t18 & t70;

    t238 = simplify(t238)
    signals.append(t238)
    t239 = t16 & t71;

    t239 = simplify(t239)
    signals.append(t239)
    t240 = t17 & t72;

    t240 = simplify(t240)
    signals.append(t240)
    t241 = t232 ^ r0_79_17537;

    t241 = simplify(t241)
    signals.append(t241)
    t242 = t241 ^ t235;

    t242 = simplify(t242)
    signals.append(t242)
    t243 = t242 ^ t238;

    t243 = simplify(t243)
    signals.append(t243)
    t244 = t243 ^ r2_79_17539;

    t244 = simplify(t244)
    signals.append(t244)
    t245 = t233 ^ r1_79_17538;

    t245 = simplify(t245)
    signals.append(t245)
    t246 = t245 ^ t236;

    t246 = simplify(t246)
    signals.append(t246)
    t247 = t246 ^ t239;

    t247 = simplify(t247)
    signals.append(t247)
    t248 = t247 ^ r0_79_17537;

    t248 = simplify(t248)
    signals.append(t248)
    t249 = t234 ^ r2_79_17539;

    t249 = simplify(t249)
    signals.append(t249)
    t250 = t249 ^ t237;

    t250 = simplify(t250)
    signals.append(t250)
    t251 = t250 ^ t240;

    t251 = simplify(t251)
    signals.append(t251)
    t252 = t251 ^ r1_79_17538;

    t252 = simplify(t252)
    signals.append(t252)
    t253 = t118 ^ t97;

    t253 = simplify(t253)
    signals.append(t253)
    t254 = t122 ^ t101;

    t254 = simplify(t254)
    signals.append(t254)
    t255 = t126 ^ t105;

    t255 = simplify(t255)
    signals.append(t255)
    t256 = t139 ^ t97;

    t256 = simplify(t256)
    signals.append(t256)
    t257 = t143 ^ t101;

    t257 = simplify(t257)
    signals.append(t257)
    t258 = t147 ^ t105;

    t258 = simplify(t258)
    signals.append(t258)
    t259 = t181 ^ t160;

    t259 = simplify(t259)
    signals.append(t259)
    t260 = t185 ^ t164;

    t260 = simplify(t260)
    signals.append(t260)
    t261 = t189 ^ t168;

    t261 = simplify(t261)
    signals.append(t261)
    t262 = t202 ^ t160;

    t262 = simplify(t262)
    signals.append(t262)
    t263 = t206 ^ t164;

    t263 = simplify(t263)
    signals.append(t263)
    t264 = t210 ^ t168;

    t264 = simplify(t264)
    signals.append(t264)
    t265 = t244 ^ t223;

    t265 = simplify(t265)
    signals.append(t265)
    t266 = t248 ^ t227;

    t266 = simplify(t266)
    signals.append(t266)
    t267 = t252 ^ t231;

    t267 = simplify(t267)
    signals.append(t267)
    t268 = t253 ^ t265;

    t268 = simplify(t268)
    signals.append(t268)
    t269 = t254 ^ t266;

    t269 = simplify(t269)
    signals.append(t269)
    t270 = t255 ^ t267;

    t270 = simplify(t270)
    signals.append(t270)
    t271 = t259 ^ t265;

    t271 = simplify(t271)
    signals.append(t271)
    t272 = t260 ^ t266;

    t272 = simplify(t272)
    signals.append(t272)
    t273 = t261 ^ t267;

    t273 = simplify(t273)
    signals.append(t273)
    t274 = t268 ^ t55;

    t274 = simplify(t274)
    signals.append(t274)
    t275 = t269 ^ t56;

    t275 = simplify(t275)
    signals.append(t275)
    t276 = t270 ^ t57;

    t276 = simplify(t276)
    signals.append(t276)
    t277 = t271 ^ t79;

    t277 = simplify(t277)
    signals.append(t277)
    t278 = t272 ^ t80;

    t278 = simplify(t278)
    signals.append(t278)
    t279 = t273 ^ t81;

    t279 = simplify(t279)
    signals.append(t279)
    t280 = t28 & t61;

    t280 = simplify(t280)
    signals.append(t280)
    t281 = t29 & t62;

    t281 = simplify(t281)
    signals.append(t281)
    t282 = t30 & t63;

    t282 = simplify(t282)
    signals.append(t282)
    t283 = t28 & t63;

    t283 = simplify(t283)
    signals.append(t283)
    t284 = t29 & t61;

    t284 = simplify(t284)
    signals.append(t284)
    t285 = t30 & t62;

    t285 = simplify(t285)
    signals.append(t285)
    t286 = t30 & t61;

    t286 = simplify(t286)
    signals.append(t286)
    t287 = t28 & t62;

    t287 = simplify(t287)
    signals.append(t287)
    t288 = t29 & t63;

    t288 = simplify(t288)
    signals.append(t288)
    t289 = t280 ^ r0_89_17540;

    t289 = simplify(t289)
    signals.append(t289)
    t290 = t289 ^ t283;

    t290 = simplify(t290)
    signals.append(t290)
    t291 = t290 ^ t286;

    t291 = simplify(t291)
    signals.append(t291)
    t292 = t291 ^ r2_89_17542;

    t292 = simplify(t292)
    signals.append(t292)
    t293 = t281 ^ r1_89_17541;

    t293 = simplify(t293)
    signals.append(t293)
    t294 = t293 ^ t284;

    t294 = simplify(t294)
    signals.append(t294)
    t295 = t294 ^ t287;

    t295 = simplify(t295)
    signals.append(t295)
    t296 = t295 ^ r0_89_17540;

    t296 = simplify(t296)
    signals.append(t296)
    t297 = t282 ^ r2_89_17542;

    t297 = simplify(t297)
    signals.append(t297)
    t298 = t297 ^ t285;

    t298 = simplify(t298)
    signals.append(t298)
    t299 = t298 ^ t288;

    t299 = simplify(t299)
    signals.append(t299)
    t300 = t299 ^ r1_89_17541;

    t300 = simplify(t300)
    signals.append(t300)
    t301 = t274 & t277;

    t301 = simplify(t301)
    signals.append(t301)
    t302 = t275 & t278;

    t302 = simplify(t302)
    signals.append(t302)
    t303 = t276 & t279;

    t303 = simplify(t303)
    signals.append(t303)
    t304 = t274 & t279;

    t304 = simplify(t304)
    signals.append(t304)
    t305 = t275 & t277;

    t305 = simplify(t305)
    signals.append(t305)
    t306 = t276 & t278;

    t306 = simplify(t306)
    signals.append(t306)
    t307 = t276 & t277;

    t307 = simplify(t307)
    signals.append(t307)
    t308 = t274 & t278;

    t308 = simplify(t308)
    signals.append(t308)
    t309 = t275 & t279;

    t309 = simplify(t309)
    signals.append(t309)
    t310 = t301 ^ r0_90_17543;

    t310 = simplify(t310)
    signals.append(t310)
    t311 = t310 ^ t304;

    t311 = simplify(t311)
    signals.append(t311)
    t312 = t311 ^ t307;

    t312 = simplify(t312)
    signals.append(t312)
    t313 = t312 ^ r2_90_17545;

    t313 = simplify(t313)
    signals.append(t313)
    t314 = t302 ^ r1_90_17544;

    t314 = simplify(t314)
    signals.append(t314)
    t315 = t314 ^ t305;

    t315 = simplify(t315)
    signals.append(t315)
    t316 = t315 ^ t308;

    t316 = simplify(t316)
    signals.append(t316)
    t317 = t316 ^ r0_90_17543;

    t317 = simplify(t317)
    signals.append(t317)
    t318 = t303 ^ r2_90_17545;

    t318 = simplify(t318)
    signals.append(t318)
    t319 = t318 ^ t306;

    t319 = simplify(t319)
    signals.append(t319)
    t320 = t319 ^ t309;

    t320 = simplify(t320)
    signals.append(t320)
    t321 = t320 ^ r1_90_17544;

    t321 = simplify(t321)
    signals.append(t321)
    t322 = t292 ^ t223;

    t322 = simplify(t322)
    signals.append(t322)
    t323 = t296 ^ t227;

    t323 = simplify(t323)
    signals.append(t323)
    t324 = t300 ^ t231;

    t324 = simplify(t324)
    signals.append(t324)
    t325 = t256 ^ t322;

    t325 = simplify(t325)
    signals.append(t325)
    t326 = t257 ^ t323;

    t326 = simplify(t326)
    signals.append(t326)
    t327 = t258 ^ t324;

    t327 = simplify(t327)
    signals.append(t327)
    t328 = t262 ^ t322;

    t328 = simplify(t328)
    signals.append(t328)
    t329 = t263 ^ t323;

    t329 = simplify(t329)
    signals.append(t329)
    t330 = t264 ^ t324;

    t330 = simplify(t330)
    signals.append(t330)
    t331 = t328 ^ t82;

    t331 = simplify(t331)
    signals.append(t331)
    t332 = t329 ^ t83;

    t332 = simplify(t332)
    signals.append(t332)
    t333 = t330 ^ t84;

    t333 = simplify(t333)
    signals.append(t333)
    t334 = t277 ^ t331;

    t334 = simplify(t334)
    signals.append(t334)
    t335 = t278 ^ t332;

    t335 = simplify(t335)
    signals.append(t335)
    t336 = t279 ^ t333;

    t336 = simplify(t336)
    signals.append(t336)
    t337 = t325 ^ t73;

    t337 = simplify(t337)
    signals.append(t337)
    t338 = t326 ^ t74;

    t338 = simplify(t338)
    signals.append(t338)
    t339 = t327 ^ t75;

    t339 = simplify(t339)
    signals.append(t339)
    t340 = t274 ^ t337;

    t340 = simplify(t340)
    signals.append(t340)
    t341 = t275 ^ t338;

    t341 = simplify(t341)
    signals.append(t341)
    t342 = t276 ^ t339;

    t342 = simplify(t342)
    signals.append(t342)
    t343 = t331 ^ t313;

    t343 = simplify(t343)
    signals.append(t343)
    t344 = t332 ^ t317;

    t344 = simplify(t344)
    signals.append(t344)
    t345 = t333 ^ t321;

    t345 = simplify(t345)
    signals.append(t345)
    t346 = t337 ^ t313;

    t346 = simplify(t346)
    signals.append(t346)
    t347 = t338 ^ t317;

    t347 = simplify(t347)
    signals.append(t347)
    t348 = t339 ^ t321;

    t348 = simplify(t348)
    signals.append(t348)
    t349 = t340 & t343;

    t349 = simplify(t349)
    signals.append(t349)
    t350 = t341 & t344;

    t350 = simplify(t350)
    signals.append(t350)
    t351 = t342 & t345;

    t351 = simplify(t351)
    signals.append(t351)
    t352 = t340 & t345;

    t352 = simplify(t352)
    signals.append(t352)
    t353 = t341 & t343;

    t353 = simplify(t353)
    signals.append(t353)
    t354 = t342 & t344;

    t354 = simplify(t354)
    signals.append(t354)
    t355 = t342 & t343;

    t355 = simplify(t355)
    signals.append(t355)
    t356 = t340 & t344;

    t356 = simplify(t356)
    signals.append(t356)
    t357 = t341 & t345;

    t357 = simplify(t357)
    signals.append(t357)
    t358 = t349 ^ r0_100_17546;

    t358 = simplify(t358)
    signals.append(t358)
    t359 = t358 ^ t352;

    t359 = simplify(t359)
    signals.append(t359)
    t360 = t359 ^ t355;

    t360 = simplify(t360)
    signals.append(t360)
    t361 = t360 ^ r2_100_17548;

    t361 = simplify(t361)
    signals.append(t361)
    t362 = t350 ^ r1_100_17547;

    t362 = simplify(t362)
    signals.append(t362)
    t363 = t362 ^ t353;

    t363 = simplify(t363)
    signals.append(t363)
    t364 = t363 ^ t356;

    t364 = simplify(t364)
    signals.append(t364)
    t365 = t364 ^ r0_100_17546;

    t365 = simplify(t365)
    signals.append(t365)
    t366 = t351 ^ r2_100_17548;

    t366 = simplify(t366)
    signals.append(t366)
    t367 = t366 ^ t354;

    t367 = simplify(t367)
    signals.append(t367)
    t368 = t367 ^ t357;

    t368 = simplify(t368)
    signals.append(t368)
    t369 = t368 ^ r1_100_17547;

    t369 = simplify(t369)
    signals.append(t369)
    t370 = t346 & t334;

    t370 = simplify(t370)
    signals.append(t370)
    t371 = t347 & t335;

    t371 = simplify(t371)
    signals.append(t371)
    t372 = t348 & t336;

    t372 = simplify(t372)
    signals.append(t372)
    t373 = t346 & t336;

    t373 = simplify(t373)
    signals.append(t373)
    t374 = t347 & t334;

    t374 = simplify(t374)
    signals.append(t374)
    t375 = t348 & t335;

    t375 = simplify(t375)
    signals.append(t375)
    t376 = t348 & t334;

    t376 = simplify(t376)
    signals.append(t376)
    t377 = t346 & t335;

    t377 = simplify(t377)
    signals.append(t377)
    t378 = t347 & t336;

    t378 = simplify(t378)
    signals.append(t378)
    t379 = t370 ^ r0_101_17549;

    t379 = simplify(t379)
    signals.append(t379)
    t380 = t379 ^ t373;

    t380 = simplify(t380)
    signals.append(t380)
    t381 = t380 ^ t376;

    t381 = simplify(t381)
    signals.append(t381)
    t382 = t381 ^ r2_101_17551;

    t382 = simplify(t382)
    signals.append(t382)
    t383 = t371 ^ r1_101_17550;

    t383 = simplify(t383)
    signals.append(t383)
    t384 = t383 ^ t374;

    t384 = simplify(t384)
    signals.append(t384)
    t385 = t384 ^ t377;

    t385 = simplify(t385)
    signals.append(t385)
    t386 = t385 ^ r0_101_17549;

    t386 = simplify(t386)
    signals.append(t386)
    t387 = t372 ^ r2_101_17551;

    t387 = simplify(t387)
    signals.append(t387)
    t388 = t387 ^ t375;

    t388 = simplify(t388)
    signals.append(t388)
    t389 = t388 ^ t378;

    t389 = simplify(t389)
    signals.append(t389)
    t390 = t389 ^ r1_101_17550;

    t390 = simplify(t390)
    signals.append(t390)
    t391 = t361 ^ t337;

    t391 = simplify(t391)
    signals.append(t391)
    t392 = t365 ^ t338;

    t392 = simplify(t392)
    signals.append(t392)
    t393 = t369 ^ t339;

    t393 = simplify(t393)
    signals.append(t393)
    t394 = t382 ^ t331;

    t394 = simplify(t394)
    signals.append(t394)
    t395 = t386 ^ t332;

    t395 = simplify(t395)
    signals.append(t395)
    t396 = t390 ^ t333;

    t396 = simplify(t396)
    signals.append(t396)
    t397 = t277 ^ t394;

    t397 = simplify(t397)
    signals.append(t397)
    t398 = t278 ^ t395;

    t398 = simplify(t398)
    signals.append(t398)
    t399 = t279 ^ t396;

    t399 = simplify(t399)
    signals.append(t399)
    t400 = t343 ^ t394;

    t400 = simplify(t400)
    signals.append(t400)
    t401 = t344 ^ t395;

    t401 = simplify(t401)
    signals.append(t401)
    t402 = t345 ^ t396;

    t402 = simplify(t402)
    signals.append(t402)
    t403 = t391 ^ t394;

    t403 = simplify(t403)
    signals.append(t403)
    t404 = t392 ^ t395;

    t404 = simplify(t404)
    signals.append(t404)
    t405 = t393 ^ t396;

    t405 = simplify(t405)
    signals.append(t405)
    t406 = t391 & t40;

    t406 = simplify(t406)
    signals.append(t406)
    t407 = t392 & t41;

    t407 = simplify(t407)
    signals.append(t407)
    t408 = t393 & t42;

    t408 = simplify(t408)
    signals.append(t408)
    t409 = t391 & t42;

    t409 = simplify(t409)
    signals.append(t409)
    t410 = t392 & t40;

    t410 = simplify(t410)
    signals.append(t410)
    t411 = t393 & t41;

    t411 = simplify(t411)
    signals.append(t411)
    t412 = t393 & t40;

    t412 = simplify(t412)
    signals.append(t412)
    t413 = t391 & t41;

    t413 = simplify(t413)
    signals.append(t413)
    t414 = t392 & t42;

    t414 = simplify(t414)
    signals.append(t414)
    t415 = t406 ^ r0_107_17552;

    t415 = simplify(t415)
    signals.append(t415)
    t416 = t415 ^ t409;

    t416 = simplify(t416)
    signals.append(t416)
    t417 = t416 ^ t412;

    t417 = simplify(t417)
    signals.append(t417)
    t418 = t417 ^ r2_107_17554;

    t418 = simplify(t418)
    signals.append(t418)
    t419 = t407 ^ r1_107_17553;

    t419 = simplify(t419)
    signals.append(t419)
    t420 = t419 ^ t410;

    t420 = simplify(t420)
    signals.append(t420)
    t421 = t420 ^ t413;

    t421 = simplify(t421)
    signals.append(t421)
    t422 = t421 ^ r0_107_17552;

    t422 = simplify(t422)
    signals.append(t422)
    t423 = t408 ^ r2_107_17554;

    t423 = simplify(t423)
    signals.append(t423)
    t424 = t423 ^ t411;

    t424 = simplify(t424)
    signals.append(t424)
    t425 = t424 ^ t414;

    t425 = simplify(t425)
    signals.append(t425)
    t426 = t425 ^ r1_107_17553;

    t426 = simplify(t426)
    signals.append(t426)
    t427 = t331 & t400;

    t427 = simplify(t427)
    signals.append(t427)
    t428 = t332 & t401;

    t428 = simplify(t428)
    signals.append(t428)
    t429 = t333 & t402;

    t429 = simplify(t429)
    signals.append(t429)
    t430 = t331 & t402;

    t430 = simplify(t430)
    signals.append(t430)
    t431 = t332 & t400;

    t431 = simplify(t431)
    signals.append(t431)
    t432 = t333 & t401;

    t432 = simplify(t432)
    signals.append(t432)
    t433 = t333 & t400;

    t433 = simplify(t433)
    signals.append(t433)
    t434 = t331 & t401;

    t434 = simplify(t434)
    signals.append(t434)
    t435 = t332 & t402;

    t435 = simplify(t435)
    signals.append(t435)
    t436 = t427 ^ r0_108_17555;

    t436 = simplify(t436)
    signals.append(t436)
    t437 = t436 ^ t430;

    t437 = simplify(t437)
    signals.append(t437)
    t438 = t437 ^ t433;

    t438 = simplify(t438)
    signals.append(t438)
    t439 = t438 ^ r2_108_17557;

    t439 = simplify(t439)
    signals.append(t439)
    t440 = t428 ^ r1_108_17556;

    t440 = simplify(t440)
    signals.append(t440)
    t441 = t440 ^ t431;

    t441 = simplify(t441)
    signals.append(t441)
    t442 = t441 ^ t434;

    t442 = simplify(t442)
    signals.append(t442)
    t443 = t442 ^ r0_108_17555;

    t443 = simplify(t443)
    signals.append(t443)
    t444 = t429 ^ r2_108_17557;

    t444 = simplify(t444)
    signals.append(t444)
    t445 = t444 ^ t432;

    t445 = simplify(t445)
    signals.append(t445)
    t446 = t445 ^ t435;

    t446 = simplify(t446)
    signals.append(t446)
    t447 = t446 ^ r1_108_17556;

    t447 = simplify(t447)
    signals.append(t447)
    t448 = t439 ^ t397;

    t448 = simplify(t448)
    signals.append(t448)
    t449 = t443 ^ t398;

    t449 = simplify(t449)
    signals.append(t449)
    t450 = t447 ^ t399;

    t450 = simplify(t450)
    signals.append(t450)
    t451 = t343 ^ t439;

    t451 = simplify(t451)
    signals.append(t451)
    t452 = t344 ^ t443;

    t452 = simplify(t452)
    signals.append(t452)
    t453 = t345 ^ t447;

    t453 = simplify(t453)
    signals.append(t453)
    t454 = t391 & t451;

    t454 = simplify(t454)
    signals.append(t454)
    t455 = t392 & t452;

    t455 = simplify(t455)
    signals.append(t455)
    t456 = t393 & t453;

    t456 = simplify(t456)
    signals.append(t456)
    t457 = t391 & t453;

    t457 = simplify(t457)
    signals.append(t457)
    t458 = t392 & t451;

    t458 = simplify(t458)
    signals.append(t458)
    t459 = t393 & t452;

    t459 = simplify(t459)
    signals.append(t459)
    t460 = t393 & t451;

    t460 = simplify(t460)
    signals.append(t460)
    t461 = t391 & t452;

    t461 = simplify(t461)
    signals.append(t461)
    t462 = t392 & t453;

    t462 = simplify(t462)
    signals.append(t462)
    t463 = t454 ^ r0_111_17558;

    t463 = simplify(t463)
    signals.append(t463)
    t464 = t463 ^ t457;

    t464 = simplify(t464)
    signals.append(t464)
    t465 = t464 ^ t460;

    t465 = simplify(t465)
    signals.append(t465)
    t466 = t465 ^ r2_111_17560;

    t466 = simplify(t466)
    signals.append(t466)
    t467 = t455 ^ r1_111_17559;

    t467 = simplify(t467)
    signals.append(t467)
    t468 = t467 ^ t458;

    t468 = simplify(t468)
    signals.append(t468)
    t469 = t468 ^ t461;

    t469 = simplify(t469)
    signals.append(t469)
    t470 = t469 ^ r0_111_17558;

    t470 = simplify(t470)
    signals.append(t470)
    t471 = t456 ^ r2_111_17560;

    t471 = simplify(t471)
    signals.append(t471)
    t472 = t471 ^ t459;

    t472 = simplify(t472)
    signals.append(t472)
    t473 = t472 ^ t462;

    t473 = simplify(t473)
    signals.append(t473)
    t474 = t473 ^ r1_111_17559;

    t474 = simplify(t474)
    signals.append(t474)
    t475 = t391 & t67;

    t475 = simplify(t475)
    signals.append(t475)
    t476 = t392 & t68;

    t476 = simplify(t476)
    signals.append(t476)
    t477 = t393 & t69;

    t477 = simplify(t477)
    signals.append(t477)
    t478 = t391 & t69;

    t478 = simplify(t478)
    signals.append(t478)
    t479 = t392 & t67;

    t479 = simplify(t479)
    signals.append(t479)
    t480 = t393 & t68;

    t480 = simplify(t480)
    signals.append(t480)
    t481 = t393 & t67;

    t481 = simplify(t481)
    signals.append(t481)
    t482 = t391 & t68;

    t482 = simplify(t482)
    signals.append(t482)
    t483 = t392 & t69;

    t483 = simplify(t483)
    signals.append(t483)
    t484 = t475 ^ r0_112_17561;

    t484 = simplify(t484)
    signals.append(t484)
    t485 = t484 ^ t478;

    t485 = simplify(t485)
    signals.append(t485)
    t486 = t485 ^ t481;

    t486 = simplify(t486)
    signals.append(t486)
    t487 = t486 ^ r2_112_17563;

    t487 = simplify(t487)
    signals.append(t487)
    t488 = t476 ^ r1_112_17562;

    t488 = simplify(t488)
    signals.append(t488)
    t489 = t488 ^ t479;

    t489 = simplify(t489)
    signals.append(t489)
    t490 = t489 ^ t482;

    t490 = simplify(t490)
    signals.append(t490)
    t491 = t490 ^ r0_112_17561;

    t491 = simplify(t491)
    signals.append(t491)
    t492 = t477 ^ r2_112_17563;

    t492 = simplify(t492)
    signals.append(t492)
    t493 = t492 ^ t480;

    t493 = simplify(t493)
    signals.append(t493)
    t494 = t493 ^ t483;

    t494 = simplify(t494)
    signals.append(t494)
    t495 = t494 ^ r1_112_17562;

    t495 = simplify(t495)
    signals.append(t495)
    t496 = t394 ^ t448;

    t496 = simplify(t496)
    signals.append(t496)
    t497 = t395 ^ t449;

    t497 = simplify(t497)
    signals.append(t497)
    t498 = t396 ^ t450;

    t498 = simplify(t498)
    signals.append(t498)
    t499 = t340 ^ t466;

    t499 = simplify(t499)
    signals.append(t499)
    t500 = t341 ^ t470;

    t500 = simplify(t500)
    signals.append(t500)
    t501 = t342 ^ t474;

    t501 = simplify(t501)
    signals.append(t501)
    t502 = t499 ^ t448;

    t502 = simplify(t502)
    signals.append(t502)
    t503 = t500 ^ t449;

    t503 = simplify(t503)
    signals.append(t503)
    t504 = t501 ^ t450;

    t504 = simplify(t504)
    signals.append(t504)
    t505 = t391 ^ t499;

    t505 = simplify(t505)
    signals.append(t505)
    t506 = t392 ^ t500;

    t506 = simplify(t506)
    signals.append(t506)
    t507 = t393 ^ t501;

    t507 = simplify(t507)
    signals.append(t507)
    t508 = t403 ^ t502;

    t508 = simplify(t508)
    signals.append(t508)
    t509 = t404 ^ t503;

    t509 = simplify(t509)
    signals.append(t509)
    t510 = t405 ^ t504;

    t510 = simplify(t510)
    signals.append(t510)
    t511 = t496 & t52;

    t511 = simplify(t511)
    signals.append(t511)
    t512 = t497 & t53;

    t512 = simplify(t512)
    signals.append(t512)
    t513 = t498 & t54;

    t513 = simplify(t513)
    signals.append(t513)
    t514 = t496 & t54;

    t514 = simplify(t514)
    signals.append(t514)
    t515 = t497 & t52;

    t515 = simplify(t515)
    signals.append(t515)
    t516 = t498 & t53;

    t516 = simplify(t516)
    signals.append(t516)
    t517 = t498 & t52;

    t517 = simplify(t517)
    signals.append(t517)
    t518 = t496 & t53;

    t518 = simplify(t518)
    signals.append(t518)
    t519 = t497 & t54;

    t519 = simplify(t519)
    signals.append(t519)
    t520 = t511 ^ r0_118_17564;

    t520 = simplify(t520)
    signals.append(t520)
    t521 = t520 ^ t514;

    t521 = simplify(t521)
    signals.append(t521)
    t522 = t521 ^ t517;

    t522 = simplify(t522)
    signals.append(t522)
    t523 = t522 ^ r2_118_17566;

    t523 = simplify(t523)
    signals.append(t523)
    t524 = t512 ^ r1_118_17565;

    t524 = simplify(t524)
    signals.append(t524)
    t525 = t524 ^ t515;

    t525 = simplify(t525)
    signals.append(t525)
    t526 = t525 ^ t518;

    t526 = simplify(t526)
    signals.append(t526)
    t527 = t526 ^ r0_118_17564;

    t527 = simplify(t527)
    signals.append(t527)
    t528 = t513 ^ r2_118_17566;

    t528 = simplify(t528)
    signals.append(t528)
    t529 = t528 ^ t516;

    t529 = simplify(t529)
    signals.append(t529)
    t530 = t529 ^ t519;

    t530 = simplify(t530)
    signals.append(t530)
    t531 = t530 ^ r1_118_17565;

    t531 = simplify(t531)
    signals.append(t531)
    t532 = t448 & t58;

    t532 = simplify(t532)
    signals.append(t532)
    t533 = t449 & t59;

    t533 = simplify(t533)
    signals.append(t533)
    t534 = t450 & t60;

    t534 = simplify(t534)
    signals.append(t534)
    t535 = t448 & t60;

    t535 = simplify(t535)
    signals.append(t535)
    t536 = t449 & t58;

    t536 = simplify(t536)
    signals.append(t536)
    t537 = t450 & t59;

    t537 = simplify(t537)
    signals.append(t537)
    t538 = t450 & t58;

    t538 = simplify(t538)
    signals.append(t538)
    t539 = t448 & t59;

    t539 = simplify(t539)
    signals.append(t539)
    t540 = t449 & t60;

    t540 = simplify(t540)
    signals.append(t540)
    t541 = t532 ^ r0_119_17567;

    t541 = simplify(t541)
    signals.append(t541)
    t542 = t541 ^ t535;

    t542 = simplify(t542)
    signals.append(t542)
    t543 = t542 ^ t538;

    t543 = simplify(t543)
    signals.append(t543)
    t544 = t543 ^ r2_119_17569;

    t544 = simplify(t544)
    signals.append(t544)
    t545 = t533 ^ r1_119_17568;

    t545 = simplify(t545)
    signals.append(t545)
    t546 = t545 ^ t536;

    t546 = simplify(t546)
    signals.append(t546)
    t547 = t546 ^ t539;

    t547 = simplify(t547)
    signals.append(t547)
    t548 = t547 ^ r0_119_17567;

    t548 = simplify(t548)
    signals.append(t548)
    t549 = t534 ^ r2_119_17569;

    t549 = simplify(t549)
    signals.append(t549)
    t550 = t549 ^ t537;

    t550 = simplify(t550)
    signals.append(t550)
    t551 = t550 ^ t540;

    t551 = simplify(t551)
    signals.append(t551)
    t552 = t551 ^ r1_119_17568;

    t552 = simplify(t552)
    signals.append(t552)
    t553 = t496 & t22;

    t553 = simplify(t553)
    signals.append(t553)
    t554 = t497 & t23;

    t554 = simplify(t554)
    signals.append(t554)
    t555 = t498 & t24;

    t555 = simplify(t555)
    signals.append(t555)
    t556 = t496 & t24;

    t556 = simplify(t556)
    signals.append(t556)
    t557 = t497 & t22;

    t557 = simplify(t557)
    signals.append(t557)
    t558 = t498 & t23;

    t558 = simplify(t558)
    signals.append(t558)
    t559 = t498 & t22;

    t559 = simplify(t559)
    signals.append(t559)
    t560 = t496 & t23;

    t560 = simplify(t560)
    signals.append(t560)
    t561 = t497 & t24;

    t561 = simplify(t561)
    signals.append(t561)
    t562 = t553 ^ r0_120_17570;

    t562 = simplify(t562)
    signals.append(t562)
    t563 = t562 ^ t556;

    t563 = simplify(t563)
    signals.append(t563)
    t564 = t563 ^ t559;

    t564 = simplify(t564)
    signals.append(t564)
    t565 = t564 ^ r2_120_17572;

    t565 = simplify(t565)
    signals.append(t565)
    t566 = t554 ^ r1_120_17571;

    t566 = simplify(t566)
    signals.append(t566)
    t567 = t566 ^ t557;

    t567 = simplify(t567)
    signals.append(t567)
    t568 = t567 ^ t560;

    t568 = simplify(t568)
    signals.append(t568)
    t569 = t568 ^ r0_120_17570;

    t569 = simplify(t569)
    signals.append(t569)
    t570 = t555 ^ r2_120_17572;

    t570 = simplify(t570)
    signals.append(t570)
    t571 = t570 ^ t558;

    t571 = simplify(t571)
    signals.append(t571)
    t572 = t571 ^ t561;

    t572 = simplify(t572)
    signals.append(t572)
    t573 = t572 ^ r1_120_17571;

    t573 = simplify(t573)
    signals.append(t573)
    t574 = t448 & t49;

    t574 = simplify(t574)
    signals.append(t574)
    t575 = t449 & t50;

    t575 = simplify(t575)
    signals.append(t575)
    t576 = t450 & t51;

    t576 = simplify(t576)
    signals.append(t576)
    t577 = t448 & t51;

    t577 = simplify(t577)
    signals.append(t577)
    t578 = t449 & t49;

    t578 = simplify(t578)
    signals.append(t578)
    t579 = t450 & t50;

    t579 = simplify(t579)
    signals.append(t579)
    t580 = t450 & t49;

    t580 = simplify(t580)
    signals.append(t580)
    t581 = t448 & t50;

    t581 = simplify(t581)
    signals.append(t581)
    t582 = t449 & t51;

    t582 = simplify(t582)
    signals.append(t582)
    t583 = t574 ^ r0_121_17573;

    t583 = simplify(t583)
    signals.append(t583)
    t584 = t583 ^ t577;

    t584 = simplify(t584)
    signals.append(t584)
    t585 = t584 ^ t580;

    t585 = simplify(t585)
    signals.append(t585)
    t586 = t585 ^ r2_121_17575;

    t586 = simplify(t586)
    signals.append(t586)
    t587 = t575 ^ r1_121_17574;

    t587 = simplify(t587)
    signals.append(t587)
    t588 = t587 ^ t578;

    t588 = simplify(t588)
    signals.append(t588)
    t589 = t588 ^ t581;

    t589 = simplify(t589)
    signals.append(t589)
    t590 = t589 ^ r0_121_17573;

    t590 = simplify(t590)
    signals.append(t590)
    t591 = t576 ^ r2_121_17575;

    t591 = simplify(t591)
    signals.append(t591)
    t592 = t591 ^ t579;

    t592 = simplify(t592)
    signals.append(t592)
    t593 = t592 ^ t582;

    t593 = simplify(t593)
    signals.append(t593)
    t594 = t593 ^ r1_121_17574;

    t594 = simplify(t594)
    signals.append(t594)
    t595 = t499 & t34;

    t595 = simplify(t595)
    signals.append(t595)
    t596 = t500 & t35;

    t596 = simplify(t596)
    signals.append(t596)
    t597 = t501 & t36;

    t597 = simplify(t597)
    signals.append(t597)
    t598 = t499 & t36;

    t598 = simplify(t598)
    signals.append(t598)
    t599 = t500 & t34;

    t599 = simplify(t599)
    signals.append(t599)
    t600 = t501 & t35;

    t600 = simplify(t600)
    signals.append(t600)
    t601 = t501 & t34;

    t601 = simplify(t601)
    signals.append(t601)
    t602 = t499 & t35;

    t602 = simplify(t602)
    signals.append(t602)
    t603 = t500 & t36;

    t603 = simplify(t603)
    signals.append(t603)
    t604 = t595 ^ r0_122_17576;

    t604 = simplify(t604)
    signals.append(t604)
    t605 = t604 ^ t598;

    t605 = simplify(t605)
    signals.append(t605)
    t606 = t605 ^ t601;

    t606 = simplify(t606)
    signals.append(t606)
    t607 = t606 ^ r2_122_17578;

    t607 = simplify(t607)
    signals.append(t607)
    t608 = t596 ^ r1_122_17577;

    t608 = simplify(t608)
    signals.append(t608)
    t609 = t608 ^ t599;

    t609 = simplify(t609)
    signals.append(t609)
    t610 = t609 ^ t602;

    t610 = simplify(t610)
    signals.append(t610)
    t611 = t610 ^ r0_122_17576;

    t611 = simplify(t611)
    signals.append(t611)
    t612 = t597 ^ r2_122_17578;

    t612 = simplify(t612)
    signals.append(t612)
    t613 = t612 ^ t600;

    t613 = simplify(t613)
    signals.append(t613)
    t614 = t613 ^ t603;

    t614 = simplify(t614)
    signals.append(t614)
    t615 = t614 ^ r1_122_17577;

    t615 = simplify(t615)
    signals.append(t615)
    t616 = t403 & t64;

    t616 = simplify(t616)
    signals.append(t616)
    t617 = t404 & t65;

    t617 = simplify(t617)
    signals.append(t617)
    t618 = t405 & t66;

    t618 = simplify(t618)
    signals.append(t618)
    t619 = t403 & t66;

    t619 = simplify(t619)
    signals.append(t619)
    t620 = t404 & t64;

    t620 = simplify(t620)
    signals.append(t620)
    t621 = t405 & t65;

    t621 = simplify(t621)
    signals.append(t621)
    t622 = t405 & t64;

    t622 = simplify(t622)
    signals.append(t622)
    t623 = t403 & t65;

    t623 = simplify(t623)
    signals.append(t623)
    t624 = t404 & t66;

    t624 = simplify(t624)
    signals.append(t624)
    t625 = t616 ^ r0_123_17579;

    t625 = simplify(t625)
    signals.append(t625)
    t626 = t625 ^ t619;

    t626 = simplify(t626)
    signals.append(t626)
    t627 = t626 ^ t622;

    t627 = simplify(t627)
    signals.append(t627)
    t628 = t627 ^ r2_123_17581;

    t628 = simplify(t628)
    signals.append(t628)
    t629 = t617 ^ r1_123_17580;

    t629 = simplify(t629)
    signals.append(t629)
    t630 = t629 ^ t620;

    t630 = simplify(t630)
    signals.append(t630)
    t631 = t630 ^ t623;

    t631 = simplify(t631)
    signals.append(t631)
    t632 = t631 ^ r0_123_17579;

    t632 = simplify(t632)
    signals.append(t632)
    t633 = t618 ^ r2_123_17581;

    t633 = simplify(t633)
    signals.append(t633)
    t634 = t633 ^ t621;

    t634 = simplify(t634)
    signals.append(t634)
    t635 = t634 ^ t624;

    t635 = simplify(t635)
    signals.append(t635)
    t636 = t635 ^ r1_123_17580;

    t636 = simplify(t636)
    signals.append(t636)
    t637 = t499 & t43;

    t637 = simplify(t637)
    signals.append(t637)
    t638 = t500 & t44;

    t638 = simplify(t638)
    signals.append(t638)
    t639 = t501 & t45;

    t639 = simplify(t639)
    signals.append(t639)
    t640 = t499 & t45;

    t640 = simplify(t640)
    signals.append(t640)
    t641 = t500 & t43;

    t641 = simplify(t641)
    signals.append(t641)
    t642 = t501 & t44;

    t642 = simplify(t642)
    signals.append(t642)
    t643 = t501 & t43;

    t643 = simplify(t643)
    signals.append(t643)
    t644 = t499 & t44;

    t644 = simplify(t644)
    signals.append(t644)
    t645 = t500 & t45;

    t645 = simplify(t645)
    signals.append(t645)
    t646 = t637 ^ r0_124_17582;

    t646 = simplify(t646)
    signals.append(t646)
    t647 = t646 ^ t640;

    t647 = simplify(t647)
    signals.append(t647)
    t648 = t647 ^ t643;

    t648 = simplify(t648)
    signals.append(t648)
    t649 = t648 ^ r2_124_17584;

    t649 = simplify(t649)
    signals.append(t649)
    t650 = t638 ^ r1_124_17583;

    t650 = simplify(t650)
    signals.append(t650)
    t651 = t650 ^ t641;

    t651 = simplify(t651)
    signals.append(t651)
    t652 = t651 ^ t644;

    t652 = simplify(t652)
    signals.append(t652)
    t653 = t652 ^ r0_124_17582;

    t653 = simplify(t653)
    signals.append(t653)
    t654 = t639 ^ r2_124_17584;

    t654 = simplify(t654)
    signals.append(t654)
    t655 = t654 ^ t642;

    t655 = simplify(t655)
    signals.append(t655)
    t656 = t655 ^ t645;

    t656 = simplify(t656)
    signals.append(t656)
    t657 = t656 ^ r1_124_17583;

    t657 = simplify(t657)
    signals.append(t657)
    t658 = t403 & t25;

    t658 = simplify(t658)
    signals.append(t658)
    t659 = t404 & t26;

    t659 = simplify(t659)
    signals.append(t659)
    t660 = t405 & t27;

    t660 = simplify(t660)
    signals.append(t660)
    t661 = t403 & t27;

    t661 = simplify(t661)
    signals.append(t661)
    t662 = t404 & t25;

    t662 = simplify(t662)
    signals.append(t662)
    t663 = t405 & t26;

    t663 = simplify(t663)
    signals.append(t663)
    t664 = t405 & t25;

    t664 = simplify(t664)
    signals.append(t664)
    t665 = t403 & t26;

    t665 = simplify(t665)
    signals.append(t665)
    t666 = t404 & t27;

    t666 = simplify(t666)
    signals.append(t666)
    t667 = t658 ^ r0_125_17585;

    t667 = simplify(t667)
    signals.append(t667)
    t668 = t667 ^ t661;

    t668 = simplify(t668)
    signals.append(t668)
    t669 = t668 ^ t664;

    t669 = simplify(t669)
    signals.append(t669)
    t670 = t669 ^ r2_125_17587;

    t670 = simplify(t670)
    signals.append(t670)
    t671 = t659 ^ r1_125_17586;

    t671 = simplify(t671)
    signals.append(t671)
    t672 = t671 ^ t662;

    t672 = simplify(t672)
    signals.append(t672)
    t673 = t672 ^ t665;

    t673 = simplify(t673)
    signals.append(t673)
    t674 = t673 ^ r0_125_17585;

    t674 = simplify(t674)
    signals.append(t674)
    t675 = t660 ^ r2_125_17587;

    t675 = simplify(t675)
    signals.append(t675)
    t676 = t675 ^ t663;

    t676 = simplify(t676)
    signals.append(t676)
    t677 = t676 ^ t666;

    t677 = simplify(t677)
    signals.append(t677)
    t678 = t677 ^ r1_125_17586;

    t678 = simplify(t678)
    signals.append(t678)
    t679 = t508 & t70;

    t679 = simplify(t679)
    signals.append(t679)
    t680 = t509 & t71;

    t680 = simplify(t680)
    signals.append(t680)
    t681 = t510 & t72;

    t681 = simplify(t681)
    signals.append(t681)
    t682 = t508 & t72;

    t682 = simplify(t682)
    signals.append(t682)
    t683 = t509 & t70;

    t683 = simplify(t683)
    signals.append(t683)
    t684 = t510 & t71;

    t684 = simplify(t684)
    signals.append(t684)
    t685 = t510 & t70;

    t685 = simplify(t685)
    signals.append(t685)
    t686 = t508 & t71;

    t686 = simplify(t686)
    signals.append(t686)
    t687 = t509 & t72;

    t687 = simplify(t687)
    signals.append(t687)
    t688 = t679 ^ r0_126_17588;

    t688 = simplify(t688)
    signals.append(t688)
    t689 = t688 ^ t682;

    t689 = simplify(t689)
    signals.append(t689)
    t690 = t689 ^ t685;

    t690 = simplify(t690)
    signals.append(t690)
    t691 = t690 ^ r2_126_17590;

    t691 = simplify(t691)
    signals.append(t691)
    t692 = t680 ^ r1_126_17589;

    t692 = simplify(t692)
    signals.append(t692)
    t693 = t692 ^ t683;

    t693 = simplify(t693)
    signals.append(t693)
    t694 = t693 ^ t686;

    t694 = simplify(t694)
    signals.append(t694)
    t695 = t694 ^ r0_126_17588;

    t695 = simplify(t695)
    signals.append(t695)
    t696 = t681 ^ r2_126_17590;

    t696 = simplify(t696)
    signals.append(t696)
    t697 = t696 ^ t684;

    t697 = simplify(t697)
    signals.append(t697)
    t698 = t697 ^ t687;

    t698 = simplify(t698)
    signals.append(t698)
    t699 = t698 ^ r1_126_17589;

    t699 = simplify(t699)
    signals.append(t699)
    t700 = t502 & t61;

    t700 = simplify(t700)
    signals.append(t700)
    t701 = t503 & t62;

    t701 = simplify(t701)
    signals.append(t701)
    t702 = t504 & t63;

    t702 = simplify(t702)
    signals.append(t702)
    t703 = t502 & t63;

    t703 = simplify(t703)
    signals.append(t703)
    t704 = t503 & t61;

    t704 = simplify(t704)
    signals.append(t704)
    t705 = t504 & t62;

    t705 = simplify(t705)
    signals.append(t705)
    t706 = t504 & t61;

    t706 = simplify(t706)
    signals.append(t706)
    t707 = t502 & t62;

    t707 = simplify(t707)
    signals.append(t707)
    t708 = t503 & t63;

    t708 = simplify(t708)
    signals.append(t708)
    t709 = t700 ^ r0_127_17591;

    t709 = simplify(t709)
    signals.append(t709)
    t710 = t709 ^ t703;

    t710 = simplify(t710)
    signals.append(t710)
    t711 = t710 ^ t706;

    t711 = simplify(t711)
    signals.append(t711)
    t712 = t711 ^ r2_127_17593;

    t712 = simplify(t712)
    signals.append(t712)
    t713 = t701 ^ r1_127_17592;

    t713 = simplify(t713)
    signals.append(t713)
    t714 = t713 ^ t704;

    t714 = simplify(t714)
    signals.append(t714)
    t715 = t714 ^ t707;

    t715 = simplify(t715)
    signals.append(t715)
    t716 = t715 ^ r0_127_17591;

    t716 = simplify(t716)
    signals.append(t716)
    t717 = t702 ^ r2_127_17593;

    t717 = simplify(t717)
    signals.append(t717)
    t718 = t717 ^ t705;

    t718 = simplify(t718)
    signals.append(t718)
    t719 = t718 ^ t708;

    t719 = simplify(t719)
    signals.append(t719)
    t720 = t719 ^ r1_127_17592;

    t720 = simplify(t720)
    signals.append(t720)
    t721 = t508 & t16;

    t721 = simplify(t721)
    signals.append(t721)
    t722 = t509 & t17;

    t722 = simplify(t722)
    signals.append(t722)
    t723 = t510 & t18;

    t723 = simplify(t723)
    signals.append(t723)
    t724 = t508 & t18;

    t724 = simplify(t724)
    signals.append(t724)
    t725 = t509 & t16;

    t725 = simplify(t725)
    signals.append(t725)
    t726 = t510 & t17;

    t726 = simplify(t726)
    signals.append(t726)
    t727 = t510 & t16;

    t727 = simplify(t727)
    signals.append(t727)
    t728 = t508 & t17;

    t728 = simplify(t728)
    signals.append(t728)
    t729 = t509 & t18;

    t729 = simplify(t729)
    signals.append(t729)
    t730 = t721 ^ r0_128_17594;

    t730 = simplify(t730)
    signals.append(t730)
    t731 = t730 ^ t724;

    t731 = simplify(t731)
    signals.append(t731)
    t732 = t731 ^ t727;

    t732 = simplify(t732)
    signals.append(t732)
    t733 = t732 ^ r2_128_17596;

    t733 = simplify(t733)
    signals.append(t733)
    t734 = t722 ^ r1_128_17595;

    t734 = simplify(t734)
    signals.append(t734)
    t735 = t734 ^ t725;

    t735 = simplify(t735)
    signals.append(t735)
    t736 = t735 ^ t728;

    t736 = simplify(t736)
    signals.append(t736)
    t737 = t736 ^ r0_128_17594;

    t737 = simplify(t737)
    signals.append(t737)
    t738 = t723 ^ r2_128_17596;

    t738 = simplify(t738)
    signals.append(t738)
    t739 = t738 ^ t726;

    t739 = simplify(t739)
    signals.append(t739)
    t740 = t739 ^ t729;

    t740 = simplify(t740)
    signals.append(t740)
    t741 = t740 ^ r1_128_17595;

    t741 = simplify(t741)
    signals.append(t741)
    t742 = t502 & t28;

    t742 = simplify(t742)
    signals.append(t742)
    t743 = t503 & t29;

    t743 = simplify(t743)
    signals.append(t743)
    t744 = t504 & t30;

    t744 = simplify(t744)
    signals.append(t744)
    t745 = t502 & t30;

    t745 = simplify(t745)
    signals.append(t745)
    t746 = t503 & t28;

    t746 = simplify(t746)
    signals.append(t746)
    t747 = t504 & t29;

    t747 = simplify(t747)
    signals.append(t747)
    t748 = t504 & t28;

    t748 = simplify(t748)
    signals.append(t748)
    t749 = t502 & t29;

    t749 = simplify(t749)
    signals.append(t749)
    t750 = t503 & t30;

    t750 = simplify(t750)
    signals.append(t750)
    t751 = t742 ^ r0_129_17597;

    t751 = simplify(t751)
    signals.append(t751)
    t752 = t751 ^ t745;

    t752 = simplify(t752)
    signals.append(t752)
    t753 = t752 ^ t748;

    t753 = simplify(t753)
    signals.append(t753)
    t754 = t753 ^ r2_129_17599;

    t754 = simplify(t754)
    signals.append(t754)
    t755 = t743 ^ r1_129_17598;

    t755 = simplify(t755)
    signals.append(t755)
    t756 = t755 ^ t746;

    t756 = simplify(t756)
    signals.append(t756)
    t757 = t756 ^ t749;

    t757 = simplify(t757)
    signals.append(t757)
    t758 = t757 ^ r0_129_17597;

    t758 = simplify(t758)
    signals.append(t758)
    t759 = t744 ^ r2_129_17599;

    t759 = simplify(t759)
    signals.append(t759)
    t760 = t759 ^ t747;

    t760 = simplify(t760)
    signals.append(t760)
    t761 = t760 ^ t750;

    t761 = simplify(t761)
    signals.append(t761)
    t762 = t761 ^ r1_129_17598;

    t762 = simplify(t762)
    signals.append(t762)
    t763 = t394 & t37;

    t763 = simplify(t763)
    signals.append(t763)
    t764 = t395 & t38;

    t764 = simplify(t764)
    signals.append(t764)
    t765 = t396 & t39;

    t765 = simplify(t765)
    signals.append(t765)
    t766 = t394 & t39;

    t766 = simplify(t766)
    signals.append(t766)
    t767 = t395 & t37;

    t767 = simplify(t767)
    signals.append(t767)
    t768 = t396 & t38;

    t768 = simplify(t768)
    signals.append(t768)
    t769 = t396 & t37;

    t769 = simplify(t769)
    signals.append(t769)
    t770 = t394 & t38;

    t770 = simplify(t770)
    signals.append(t770)
    t771 = t395 & t39;

    t771 = simplify(t771)
    signals.append(t771)
    t772 = t763 ^ r0_130_175100;

    t772 = simplify(t772)
    signals.append(t772)
    t773 = t772 ^ t766;

    t773 = simplify(t773)
    signals.append(t773)
    t774 = t773 ^ t769;

    t774 = simplify(t774)
    signals.append(t774)
    t775 = t774 ^ r2_130_175102;

    t775 = simplify(t775)
    signals.append(t775)
    t776 = t764 ^ r1_130_175101;

    t776 = simplify(t776)
    signals.append(t776)
    t777 = t776 ^ t767;

    t777 = simplify(t777)
    signals.append(t777)
    t778 = t777 ^ t770;

    t778 = simplify(t778)
    signals.append(t778)
    t779 = t778 ^ r0_130_175100;

    t779 = simplify(t779)
    signals.append(t779)
    t780 = t765 ^ r2_130_175102;

    t780 = simplify(t780)
    signals.append(t780)
    t781 = t780 ^ t768;

    t781 = simplify(t781)
    signals.append(t781)
    t782 = t781 ^ t771;

    t782 = simplify(t782)
    signals.append(t782)
    t783 = t782 ^ r1_130_175101;

    t783 = simplify(t783)
    signals.append(t783)
    t784 = t505 & t19;

    t784 = simplify(t784)
    signals.append(t784)
    t785 = t506 & t20;

    t785 = simplify(t785)
    signals.append(t785)
    t786 = t507 & t21;

    t786 = simplify(t786)
    signals.append(t786)
    t787 = t505 & t21;

    t787 = simplify(t787)
    signals.append(t787)
    t788 = t506 & t19;

    t788 = simplify(t788)
    signals.append(t788)
    t789 = t507 & t20;

    t789 = simplify(t789)
    signals.append(t789)
    t790 = t507 & t19;

    t790 = simplify(t790)
    signals.append(t790)
    t791 = t505 & t20;

    t791 = simplify(t791)
    signals.append(t791)
    t792 = t506 & t21;

    t792 = simplify(t792)
    signals.append(t792)
    t793 = t784 ^ r0_131_175103;

    t793 = simplify(t793)
    signals.append(t793)
    t794 = t793 ^ t787;

    t794 = simplify(t794)
    signals.append(t794)
    t795 = t794 ^ t790;

    t795 = simplify(t795)
    signals.append(t795)
    t796 = t795 ^ r2_131_175105;

    t796 = simplify(t796)
    signals.append(t796)
    t797 = t785 ^ r1_131_175104;

    t797 = simplify(t797)
    signals.append(t797)
    t798 = t797 ^ t788;

    t798 = simplify(t798)
    signals.append(t798)
    t799 = t798 ^ t791;

    t799 = simplify(t799)
    signals.append(t799)
    t800 = t799 ^ r0_131_175103;

    t800 = simplify(t800)
    signals.append(t800)
    t801 = t786 ^ r2_131_175105;

    t801 = simplify(t801)
    signals.append(t801)
    t802 = t801 ^ t789;

    t802 = simplify(t802)
    signals.append(t802)
    t803 = t802 ^ t792;

    t803 = simplify(t803)
    signals.append(t803)
    t804 = t803 ^ r1_131_175104;

    t804 = simplify(t804)
    signals.append(t804)
    t805 = t394 & r_17214;

    t805 = simplify(t805)
    signals.append(t805)
    t806 = t395 & r_17215;

    t806 = simplify(t806)
    signals.append(t806)
    t807 = t396 & t15;

    t807 = simplify(t807)
    signals.append(t807)
    t808 = t394 & t15;

    t808 = simplify(t808)
    signals.append(t808)
    t809 = t395 & r_17214;

    t809 = simplify(t809)
    signals.append(t809)
    t810 = t396 & r_17215;

    t810 = simplify(t810)
    signals.append(t810)
    t811 = t396 & r_17214;

    t811 = simplify(t811)
    signals.append(t811)
    t812 = t394 & r_17215;

    t812 = simplify(t812)
    signals.append(t812)
    t813 = t395 & t15;

    t813 = simplify(t813)
    signals.append(t813)
    t814 = t805 ^ r0_132_175106;

    t814 = simplify(t814)
    signals.append(t814)
    t815 = t814 ^ t808;

    t815 = simplify(t815)
    signals.append(t815)
    t816 = t815 ^ t811;

    t816 = simplify(t816)
    signals.append(t816)
    t817 = t816 ^ r2_132_175108;

    t817 = simplify(t817)
    signals.append(t817)
    t818 = t806 ^ r1_132_175107;

    t818 = simplify(t818)
    signals.append(t818)
    t819 = t818 ^ t809;

    t819 = simplify(t819)
    signals.append(t819)
    t820 = t819 ^ t812;

    t820 = simplify(t820)
    signals.append(t820)
    t821 = t820 ^ r0_132_175106;

    t821 = simplify(t821)
    signals.append(t821)
    t822 = t807 ^ r2_132_175108;

    t822 = simplify(t822)
    signals.append(t822)
    t823 = t822 ^ t810;

    t823 = simplify(t823)
    signals.append(t823)
    t824 = t823 ^ t813;

    t824 = simplify(t824)
    signals.append(t824)
    t825 = t824 ^ r1_132_175107;

    t825 = simplify(t825)
    signals.append(t825)
    t826 = t505 & t76;

    t826 = simplify(t826)
    signals.append(t826)
    t827 = t506 & t77;

    t827 = simplify(t827)
    signals.append(t827)
    t828 = t507 & t78;

    t828 = simplify(t828)
    signals.append(t828)
    t829 = t505 & t78;

    t829 = simplify(t829)
    signals.append(t829)
    t830 = t506 & t76;

    t830 = simplify(t830)
    signals.append(t830)
    t831 = t507 & t77;

    t831 = simplify(t831)
    signals.append(t831)
    t832 = t507 & t76;

    t832 = simplify(t832)
    signals.append(t832)
    t833 = t505 & t77;

    t833 = simplify(t833)
    signals.append(t833)
    t834 = t506 & t78;

    t834 = simplify(t834)
    signals.append(t834)
    t835 = t826 ^ r0_133_175109;

    t835 = simplify(t835)
    signals.append(t835)
    t836 = t835 ^ t829;

    t836 = simplify(t836)
    signals.append(t836)
    t837 = t836 ^ t832;

    t837 = simplify(t837)
    signals.append(t837)
    t838 = t837 ^ r2_133_175111;

    t838 = simplify(t838)
    signals.append(t838)
    t839 = t827 ^ r1_133_175110;

    t839 = simplify(t839)
    signals.append(t839)
    t840 = t839 ^ t830;

    t840 = simplify(t840)
    signals.append(t840)
    t841 = t840 ^ t833;

    t841 = simplify(t841)
    signals.append(t841)
    t842 = t841 ^ r0_133_175109;

    t842 = simplify(t842)
    signals.append(t842)
    t843 = t828 ^ r2_133_175111;

    t843 = simplify(t843)
    signals.append(t843)
    t844 = t843 ^ t831;

    t844 = simplify(t844)
    signals.append(t844)
    t845 = t844 ^ t834;

    t845 = simplify(t845)
    signals.append(t845)
    t846 = t845 ^ r1_133_175110;

    t846 = simplify(t846)
    signals.append(t846)
    t847 = t670 ^ t733;

    t847 = simplify(t847)
    signals.append(t847)
    t848 = t674 ^ t737;

    t848 = simplify(t848)
    signals.append(t848)
    t849 = t678 ^ t741;

    t849 = simplify(t849)
    signals.append(t849)
    t850 = t586 ^ t775;

    t850 = simplify(t850)
    signals.append(t850)
    t851 = t590 ^ t779;

    t851 = simplify(t851)
    signals.append(t851)
    t852 = t594 ^ t783;

    t852 = simplify(t852)
    signals.append(t852)
    t853 = t487 ^ t649;

    t853 = simplify(t853)
    signals.append(t853)
    t854 = t491 ^ t653;

    t854 = simplify(t854)
    signals.append(t854)
    t855 = t495 ^ t657;

    t855 = simplify(t855)
    signals.append(t855)
    t856 = t565 ^ t586;

    t856 = simplify(t856)
    signals.append(t856)
    t857 = t569 ^ t590;

    t857 = simplify(t857)
    signals.append(t857)
    t858 = t573 ^ t594;

    t858 = simplify(t858)
    signals.append(t858)
    t859 = t817 ^ t796;

    t859 = simplify(t859)
    signals.append(t859)
    t860 = t821 ^ t800;

    t860 = simplify(t860)
    signals.append(t860)
    t861 = t825 ^ t804;

    t861 = simplify(t861)
    signals.append(t861)
    t862 = t817 ^ t487;

    t862 = simplify(t862)
    signals.append(t862)
    t863 = t821 ^ t491;

    t863 = simplify(t863)
    signals.append(t863)
    t864 = t825 ^ t495;

    t864 = simplify(t864)
    signals.append(t864)
    t865 = t691 ^ t712;

    t865 = simplify(t865)
    signals.append(t865)
    t866 = t695 ^ t716;

    t866 = simplify(t866)
    signals.append(t866)
    t867 = t699 ^ t720;

    t867 = simplify(t867)
    signals.append(t867)
    t868 = t523 ^ t838;

    t868 = simplify(t868)
    signals.append(t868)
    t869 = t527 ^ t842;

    t869 = simplify(t869)
    signals.append(t869)
    t870 = t531 ^ t846;

    t870 = simplify(t870)
    signals.append(t870)
    t871 = t628 ^ t691;

    t871 = simplify(t871)
    signals.append(t871)
    t872 = t632 ^ t695;

    t872 = simplify(t872)
    signals.append(t872)
    t873 = t636 ^ t699;

    t873 = simplify(t873)
    signals.append(t873)
    t874 = t733 ^ t754;

    t874 = simplify(t874)
    signals.append(t874)
    t875 = t737 ^ t758;

    t875 = simplify(t875)
    signals.append(t875)
    t876 = t741 ^ t762;

    t876 = simplify(t876)
    signals.append(t876)
    t877 = t796 ^ t853;

    t877 = simplify(t877)
    signals.append(t877)
    t878 = t800 ^ t854;

    t878 = simplify(t878)
    signals.append(t878)
    t879 = t804 ^ t855;

    t879 = simplify(t879)
    signals.append(t879)
    t880 = t859 ^ t868;

    t880 = simplify(t880)
    signals.append(t880)
    t881 = t860 ^ t869;

    t881 = simplify(t881)
    signals.append(t881)
    t882 = t861 ^ t870;

    t882 = simplify(t882)
    signals.append(t882)
    t883 = t607 ^ t847;

    t883 = simplify(t883)
    signals.append(t883)
    t884 = t611 ^ t848;

    t884 = simplify(t884)
    signals.append(t884)
    t885 = t615 ^ t849;

    t885 = simplify(t885)
    signals.append(t885)
    t886 = t838 ^ t871;

    t886 = simplify(t886)
    signals.append(t886)
    t887 = t842 ^ t872;

    t887 = simplify(t887)
    signals.append(t887)
    t888 = t846 ^ t873;

    t888 = simplify(t888)
    signals.append(t888)
    t889 = t847 ^ t880;

    t889 = simplify(t889)
    signals.append(t889)
    t890 = t848 ^ t881;

    t890 = simplify(t890)
    signals.append(t890)
    t891 = t849 ^ t882;

    t891 = simplify(t891)
    signals.append(t891)
    t892 = t418 ^ t880;

    t892 = simplify(t892)
    signals.append(t892)
    t893 = t422 ^ t881;

    t893 = simplify(t893)
    signals.append(t893)
    t894 = t426 ^ t882;

    t894 = simplify(t894)
    signals.append(t894)
    t895 = t865 ^ t883;

    t895 = simplify(t895)
    signals.append(t895)
    t896 = t866 ^ t884;

    t896 = simplify(t896)
    signals.append(t896)
    t897 = t867 ^ t885;

    t897 = simplify(t897)
    signals.append(t897)
    t898 = t856 ^ t883;

    t898 = simplify(t898)
    signals.append(t898)
    t899 = t857 ^ t884;

    t899 = simplify(t899)
    signals.append(t899)
    t900 = t858 ^ t885;

    t900 = simplify(t900)
    signals.append(t900)
    t901 = t607 ^ t886;

    t901 = simplify(t901)
    signals.append(t901)
    t902 = t611 ^ t887;

    t902 = simplify(t902)
    signals.append(t902)
    t903 = t615 ^ t888;

    t903 = simplify(t903)
    signals.append(t903)
    t904 = t892 ^ t895;

    t904 = simplify(t904)
    signals.append(t904)
    t905 = t893 ^ t896;

    t905 = simplify(t905)
    signals.append(t905)
    t906 = t894 ^ t897;

    t906 = simplify(t906)
    signals.append(t906)
    t907 = t544 ^ t898;

    t907 = simplify(t907)
    signals.append(t907)
    t908 = t548 ^ t899;

    t908 = simplify(t908)
    signals.append(t908)
    t909 = t552 ^ t900;

    t909 = simplify(t909)
    signals.append(t909)
    t910 = t886 ^ t898;

    t910 = simplify(t910)
    signals.append(t910)
    t911 = t887 ^ t899;

    t911 = simplify(t911)
    signals.append(t911)
    t912 = t888 ^ t900;

    t912 = simplify(t912)
    signals.append(t912)
    t913 = t877 ^ t895;

    t913 = simplify(t913)
    signals.append(t913)
    t914 = t878 ^ t896;

    t914 = simplify(t914)
    signals.append(t914)
    t915 = t879 ^ t897;

    t915 = simplify(t915)
    signals.append(t915)
    t916 = t853 ^ t889;

    t916 = simplify(t916)
    signals.append(t916)
    t917 = t854 ^ t890;

    t917 = simplify(t917)
    signals.append(t917)
    t918 = t855 ^ t891;

    t918 = simplify(t918)
    signals.append(t918)
    t919 = t901 ^ t904;

    t919 = simplify(t919)
    signals.append(t919)
    t920 = t902 ^ t905;

    t920 = simplify(t920)
    signals.append(t920)
    t921 = t903 ^ t906;

    t921 = simplify(t921)
    signals.append(t921)
    t922 = t868 ^ t907;

    t922 = simplify(t922)
    signals.append(t922)
    t923 = t869 ^ t908;

    t923 = simplify(t923)
    signals.append(t923)
    t924 = t870 ^ t909;

    t924 = simplify(t924)
    signals.append(t924)
    t925 = t862 ^ t907;

    t925 = simplify(t925)
    signals.append(t925)
    t926 = t863 ^ t908;

    t926 = simplify(t926)
    signals.append(t926)
    t927 = t864 ^ t909;

    t927 = simplify(t927)
    signals.append(t927)
    t928 = t850 ^ t904;

    t928 = simplify(t928)
    signals.append(t928)
    t929 = t851 ^ t905;

    t929 = simplify(t929)
    signals.append(t929)
    t930 = t852 ^ t906;

    t930 = simplify(t930)
    signals.append(t930)
    t931 = t901 ^ t922;

    t931 = simplify(t931)
    signals.append(t931)
    t932 = t902 ^ t923;

    t932 = simplify(t932)
    signals.append(t932)
    t933 = t903 ^ t924;

    t933 = simplify(t933)
    signals.append(t933)
    t934 = t874 ^ t919;

    t934 = simplify(t934)
    signals.append(t934)
    t935 = t875 ^ t920;

    t935 = simplify(t935)
    signals.append(t935)
    t936 = t876 ^ t921;

    t936 = simplify(t936)
    signals.append(t936)


    if firstOrder:
        nbExps = 0
        nbLeak = 0
        print('# First Order Analysis')
        i = 0
        for s0idx in range(len(signals)):
            i = i + 1
            print i
            print len(signals)
            checkExpLeakageFirstOrder(signals[s0idx])

        print('# Nb. expressions analysed: %d' % nbExps)
        print('# Nb. expressions leaking: %d' % nbLeak)



    if secondOrder:
        nbExps = 0
        nbLeak = 0
        print('# Second Order Analysis')
        for s0idx in range(len(signals)):
            for s1idx in range(s0idx + 1, len(signals)):
                checkExpLeakageSecondOrder(signals[s0idx], signals[s1idx])

        print('# Nb. expressions analysed: %d' % nbExps)
        print('# Nb. expressions leaking: %d' % nbLeak)




if __name__ == '__main__':

    testLitteral = False

    if not testLitteral:


        k0 = symbol('k0', 'S', 1)
        k1 = symbol('k1', 'S', 1)
        k2 = symbol('k2', 'S', 1)
        k3 = symbol('k3', 'S', 1)
        k4 = symbol('k4', 'S', 1)
        k5 = symbol('k5', 'S', 1)
        k6 = symbol('k6', 'S', 1)
        k7 = symbol('k7', 'S', 1)

        uma1(k0, k1, k2, k3, k4, k5, k6, k7)

    else:
        def enumerate_values(t, currIdx):
            if currIdx == len(t):
                m0 = constant(t[0], 1)
                m1 = constant(t[1], 1)
                z12 = constant(t[2], 1)
                r0 = constant(t[3], 1)
                r1 = constant(t[4], 1)
                k0 = constant(t[5], 1)
                k1 = constant(t[6], 1)

                c1, c2 = isw_and_2s_norand(m0, m1, z12, r0, r1, k0, k1)
 
                r_ref = k0 & k1
                r_ref = simplify(r_ref)
                r = c1 ^ c2
                r = simplify(r)

                if '%s' % r_ref != '%s' % r:
                    print('*** Error for values (%s, %s, %s, %s, %s, %s, %s): result is %s instead of %s' % (m0, m1, z12, r0, r1, k0, k1, r, r_ref))
                    sys.exit(0)
            else:
                t[currIdx] = 0
                enumerate_values(t, currIdx + 1)
                t[currIdx] = 1
                enumerate_values(t, currIdx + 1)

        t = [0] * 7
        enumerate_values(t, 0)
        print('[OK]')


