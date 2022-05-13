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
from utils import *
from check_leakage import *
from config import *

def mySimplify(e):
    if True:
        return simp(e)
    else:
        return e

nbExps = 0
nbLeak = 0

firstOrder = True
secondOrder = False

def checkExpLeakageFirstOrder(e0):
    global nbExps
    global nbLeak
    res, usedBitExp, niTime = checkNIVal(e0)
    print niTime
    nbExps += 1
    if not res:
        nbLeak += 1

    if not res:
        print('# Leakage exp num %d' % (nbExps))


def checkExpLeakageSecondOrder(e0, e1):
    global nbExps
    global nbLeak
    res, usedBitExp, niTime = checkNITrans(e0, e1)
    nbExps += 1
    if not res:
        nbLeak += 1

    if not res:
        print('# Leakage for exp num %d' % (nbExps))



def uma1(k0, k1, k2, k3, k4, k5, k6, k7):
    global nbExps
    global nbLeak

    r_1800 = symbol('r_1800', 'M', 1)
    r_1801 = symbol('r_1801', 'M', 1)
    r_1802 = symbol('r_1802', 'M', 1)
    r_1803 = symbol('r_1803', 'M', 1)
    r_1804 = symbol('r_1804', 'M', 1)
    r_1805 = symbol('r_1805', 'M', 1)
    r_1806 = symbol('r_1806', 'M', 1)
    r_1807 = symbol('r_1807', 'M', 1)
    r_1808 = symbol('r_1808', 'M', 1)
    r_1809 = symbol('r_1809', 'M', 1)
    r_18010 = symbol('r_18010', 'M', 1)
    r_18011 = symbol('r_18011', 'M', 1)
    r_18012 = symbol('r_18012', 'M', 1)
    r_18013 = symbol('r_18013', 'M', 1)
    r_18014 = symbol('r_18014', 'M', 1)
    r_18015 = symbol('r_18015', 'M', 1)
    r0_80_18316 = symbol('r0_80_18316', 'M', 1)
    r1_80_18317 = symbol('r1_80_18317', 'M', 1)
    r0_81_18318 = symbol('r0_81_18318', 'M', 1)
    r1_81_18319 = symbol('r1_81_18319', 'M', 1)
    r0_82_18320 = symbol('r0_82_18320', 'M', 1)
    r1_82_18321 = symbol('r1_82_18321', 'M', 1)
    r0_83_18322 = symbol('r0_83_18322', 'M', 1)
    r1_83_18323 = symbol('r1_83_18323', 'M', 1)
    r0_84_18324 = symbol('r0_84_18324', 'M', 1)
    r1_84_18325 = symbol('r1_84_18325', 'M', 1)
    r0_85_18326 = symbol('r0_85_18326', 'M', 1)
    r1_85_18327 = symbol('r1_85_18327', 'M', 1)
    r0_86_18328 = symbol('r0_86_18328', 'M', 1)
    r1_86_18329 = symbol('r1_86_18329', 'M', 1)
    r0_87_18330 = symbol('r0_87_18330', 'M', 1)
    r1_87_18331 = symbol('r1_87_18331', 'M', 1)
    r0_97_18332 = symbol('r0_97_18332', 'M', 1)
    r1_97_18333 = symbol('r1_97_18333', 'M', 1)
    r0_98_18334 = symbol('r0_98_18334', 'M', 1)
    r1_98_18335 = symbol('r1_98_18335', 'M', 1)
    r0_108_18336 = symbol('r0_108_18336', 'M', 1)
    r1_108_18337 = symbol('r1_108_18337', 'M', 1)
    r0_109_18338 = symbol('r0_109_18338', 'M', 1)
    r1_109_18339 = symbol('r1_109_18339', 'M', 1)
    r0_115_18340 = symbol('r0_115_18340', 'M', 1)
    r1_115_18341 = symbol('r1_115_18341', 'M', 1)
    r0_116_18342 = symbol('r0_116_18342', 'M', 1)
    r1_116_18343 = symbol('r1_116_18343', 'M', 1)
    r0_119_18344 = symbol('r0_119_18344', 'M', 1)
    r1_119_18345 = symbol('r1_119_18345', 'M', 1)
    r0_120_18346 = symbol('r0_120_18346', 'M', 1)
    r1_120_18347 = symbol('r1_120_18347', 'M', 1)
    r0_126_18348 = symbol('r0_126_18348', 'M', 1)
    r1_126_18349 = symbol('r1_126_18349', 'M', 1)
    r0_127_18350 = symbol('r0_127_18350', 'M', 1)
    r1_127_18351 = symbol('r1_127_18351', 'M', 1)
    r0_128_18352 = symbol('r0_128_18352', 'M', 1)
    r1_128_18353 = symbol('r1_128_18353', 'M', 1)
    r0_129_18354 = symbol('r0_129_18354', 'M', 1)
    r1_129_18355 = symbol('r1_129_18355', 'M', 1)
    r0_130_18356 = symbol('r0_130_18356', 'M', 1)
    r1_130_18357 = symbol('r1_130_18357', 'M', 1)
    r0_131_18358 = symbol('r0_131_18358', 'M', 1)
    r1_131_18359 = symbol('r1_131_18359', 'M', 1)
    r0_132_18360 = symbol('r0_132_18360', 'M', 1)
    r1_132_18361 = symbol('r1_132_18361', 'M', 1)
    r0_133_18362 = symbol('r0_133_18362', 'M', 1)
    r1_133_18363 = symbol('r1_133_18363', 'M', 1)
    r0_134_18364 = symbol('r0_134_18364', 'M', 1)
    r1_134_18365 = symbol('r1_134_18365', 'M', 1)
    r0_135_18366 = symbol('r0_135_18366', 'M', 1)
    r1_135_18367 = symbol('r1_135_18367', 'M', 1)
    r0_136_18368 = symbol('r0_136_18368', 'M', 1)
    r1_136_18369 = symbol('r1_136_18369', 'M', 1)
    r0_137_18370 = symbol('r0_137_18370', 'M', 1)
    r1_137_18371 = symbol('r1_137_18371', 'M', 1)
    r0_138_18372 = symbol('r0_138_18372', 'M', 1)
    r1_138_18373 = symbol('r1_138_18373', 'M', 1)
    r0_139_18374 = symbol('r0_139_18374', 'M', 1)
    r1_139_18375 = symbol('r1_139_18375', 'M', 1)
    r0_140_18376 = symbol('r0_140_18376', 'M', 1)
    r1_140_18377 = symbol('r1_140_18377', 'M', 1)
    r0_141_18378 = symbol('r0_141_18378', 'M', 1)
    r1_141_18379 = symbol('r1_141_18379', 'M', 1)
    signals = []
    presharing0 = k0 ^ r_1800;

    presharing0 = mySimplify(presharing0)
    signals.append(presharing0)
    t1 = presharing0 ^ r_1801;

    t1 = mySimplify(t1)
    signals.append(t1)
    presharing2 = k1 ^ r_1802;

    presharing2 = mySimplify(presharing2)
    signals.append(presharing2)
    t3 = presharing2 ^ r_1803;

    t3 = mySimplify(t3)
    signals.append(t3)
    presharing4 = k2 ^ r_1804;

    presharing4 = mySimplify(presharing4)
    signals.append(presharing4)
    t5 = presharing4 ^ r_1805;

    t5 = mySimplify(t5)
    signals.append(t5)
    presharing6 = k3 ^ r_1806;

    presharing6 = mySimplify(presharing6)
    signals.append(presharing6)
    t7 = presharing6 ^ r_1807;

    t7 = mySimplify(t7)
    signals.append(t7)
    presharing8 = k4 ^ r_1808;

    presharing8 = mySimplify(presharing8)
    signals.append(presharing8)
    t9 = presharing8 ^ r_1809;

    t9 = mySimplify(t9)
    signals.append(t9)
    presharing10 = k5 ^ r_18010;

    presharing10 = mySimplify(presharing10)
    signals.append(presharing10)
    t11 = presharing10 ^ r_18011;

    t11 = mySimplify(t11)
    signals.append(t11)
    presharing12 = k6 ^ r_18012;

    presharing12 = mySimplify(presharing12)
    signals.append(presharing12)
    t13 = presharing12 ^ r_18013;

    t13 = mySimplify(t13)
    signals.append(t13)
    presharing14 = k7 ^ r_18014;

    presharing14 = mySimplify(presharing14)
    signals.append(presharing14)
    t15 = presharing14 ^ r_18015;

    t15 = mySimplify(t15)
    signals.append(t15)
    t16 = r_1806 ^ r_18010;

    t16 = mySimplify(t16)
    signals.append(t16)
    t17 = r_1807 ^ r_18011;

    t17 = mySimplify(t17)
    signals.append(t17)
    t18 = t7 ^ t11;

    t18 = mySimplify(t18)
    signals.append(t18)
    t19 = r_1800 ^ r_18012;

    t19 = mySimplify(t19)
    signals.append(t19)
    t20 = r_1801 ^ r_18013;

    t20 = mySimplify(t20)
    signals.append(t20)
    t21 = t1 ^ t13;

    t21 = mySimplify(t21)
    signals.append(t21)
    t22 = t19 ^ t16;

    t22 = mySimplify(t22)
    signals.append(t22)
    t23 = t20 ^ t17;

    t23 = mySimplify(t23)
    signals.append(t23)
    t24 = t21 ^ t18;

    t24 = mySimplify(t24)
    signals.append(t24)
    t25 = r_1800 ^ r_1806;

    t25 = mySimplify(t25)
    signals.append(t25)
    t26 = r_1801 ^ r_1807;

    t26 = mySimplify(t26)
    signals.append(t26)
    t27 = t1 ^ t7;

    t27 = mySimplify(t27)
    signals.append(t27)
    t28 = r_1800 ^ r_18010;

    t28 = mySimplify(t28)
    signals.append(t28)
    t29 = r_1801 ^ r_18011;

    t29 = mySimplify(t29)
    signals.append(t29)
    t30 = t1 ^ t11;

    t30 = mySimplify(t30)
    signals.append(t30)
    t31 = r_1802 ^ r_1804;

    t31 = mySimplify(t31)
    signals.append(t31)
    t32 = r_1803 ^ r_1805;

    t32 = mySimplify(t32)
    signals.append(t32)
    t33 = t3 ^ t5;

    t33 = mySimplify(t33)
    signals.append(t33)
    t34 = t31 ^ r_18014;

    t34 = mySimplify(t34)
    signals.append(t34)
    t35 = t32 ^ r_18015;

    t35 = mySimplify(t35)
    signals.append(t35)
    t36 = t33 ^ t15;

    t36 = mySimplify(t36)
    signals.append(t36)
    t37 = t34 ^ r_1806;

    t37 = mySimplify(t37)
    signals.append(t37)
    t38 = t35 ^ r_1807;

    t38 = mySimplify(t38)
    signals.append(t38)
    t39 = t36 ^ t7;

    t39 = mySimplify(t39)
    signals.append(t39)
    t40 = t34 ^ r_1800;

    t40 = mySimplify(t40)
    signals.append(t40)
    t41 = t35 ^ r_1801;

    t41 = mySimplify(t41)
    signals.append(t41)
    t42 = t36 ^ t1;

    t42 = mySimplify(t42)
    signals.append(t42)
    t43 = t34 ^ r_18012;

    t43 = mySimplify(t43)
    signals.append(t43)
    t44 = t35 ^ r_18013;

    t44 = mySimplify(t44)
    signals.append(t44)
    t45 = t36 ^ t13;

    t45 = mySimplify(t45)
    signals.append(t45)
    t46 = r_1808 ^ t22;

    t46 = mySimplify(t46)
    signals.append(t46)
    t47 = r_1809 ^ t23;

    t47 = mySimplify(t47)
    signals.append(t47)
    t48 = t9 ^ t24;

    t48 = mySimplify(t48)
    signals.append(t48)
    t49 = t43 ^ t28;

    t49 = mySimplify(t49)
    signals.append(t49)
    t50 = t44 ^ t29;

    t50 = mySimplify(t50)
    signals.append(t50)
    t51 = t45 ^ t30;

    t51 = mySimplify(t51)
    signals.append(t51)
    t52 = t46 ^ r_18010;

    t52 = mySimplify(t52)
    signals.append(t52)
    t53 = t47 ^ r_18011;

    t53 = mySimplify(t53)
    signals.append(t53)
    t54 = t48 ^ t11;

    t54 = mySimplify(t54)
    signals.append(t54)
    t55 = t46 ^ r_1802;

    t55 = mySimplify(t55)
    signals.append(t55)
    t56 = t47 ^ r_1803;

    t56 = mySimplify(t56)
    signals.append(t56)
    t57 = t48 ^ t3;

    t57 = mySimplify(t57)
    signals.append(t57)
    t58 = t52 ^ r_18014;

    t58 = mySimplify(t58)
    signals.append(t58)
    t59 = t53 ^ r_18015;

    t59 = mySimplify(t59)
    signals.append(t59)
    t60 = t54 ^ t15;

    t60 = mySimplify(t60)
    signals.append(t60)
    t61 = t52 ^ t31;

    t61 = mySimplify(t61)
    signals.append(t61)
    t62 = t53 ^ t32;

    t62 = mySimplify(t62)
    signals.append(t62)
    t63 = t54 ^ t33;

    t63 = mySimplify(t63)
    signals.append(t63)
    t64 = t55 ^ t25;

    t64 = mySimplify(t64)
    signals.append(t64)
    t65 = t56 ^ t26;

    t65 = mySimplify(t65)
    signals.append(t65)
    t66 = t57 ^ t27;

    t66 = mySimplify(t66)
    signals.append(t66)
    t67 = r_18014 ^ t64;

    t67 = mySimplify(t67)
    signals.append(t67)
    t68 = r_18015 ^ t65;

    t68 = mySimplify(t68)
    signals.append(t68)
    t69 = t15 ^ t66;

    t69 = mySimplify(t69)
    signals.append(t69)
    t70 = t61 ^ t64;

    t70 = mySimplify(t70)
    signals.append(t70)
    t71 = t62 ^ t65;

    t71 = mySimplify(t71)
    signals.append(t71)
    t72 = t63 ^ t66;

    t72 = mySimplify(t72)
    signals.append(t72)
    t73 = t61 ^ t28;

    t73 = mySimplify(t73)
    signals.append(t73)
    t74 = t62 ^ t29;

    t74 = mySimplify(t74)
    signals.append(t74)
    t75 = t63 ^ t30;

    t75 = mySimplify(t75)
    signals.append(t75)
    t76 = t31 ^ t64;

    t76 = mySimplify(t76)
    signals.append(t76)
    t77 = t32 ^ t65;

    t77 = mySimplify(t77)
    signals.append(t77)
    t78 = t33 ^ t66;

    t78 = mySimplify(t78)
    signals.append(t78)
    t79 = t19 ^ t76;

    t79 = mySimplify(t79)
    signals.append(t79)
    t80 = t20 ^ t77;

    t80 = mySimplify(t80)
    signals.append(t80)
    t81 = t21 ^ t78;

    t81 = mySimplify(t81)
    signals.append(t81)
    t82 = r_1800 ^ t76;

    t82 = mySimplify(t82)
    signals.append(t82)
    t83 = r_1801 ^ t77;

    t83 = mySimplify(t83)
    signals.append(t83)
    t84 = t1 ^ t78;

    t84 = mySimplify(t84)
    signals.append(t84)
    t85 = t22 & t52;

    t85 = mySimplify(t85)
    signals.append(t85)
    t86 = t85 ^ r0_80_18316;

    t86 = mySimplify(t86)
    signals.append(t86)
    t87 = t22 & t54;

    t87 = mySimplify(t87)
    signals.append(t87)
    t88 = t86 ^ t87;

    t88 = mySimplify(t88)
    signals.append(t88)
    t89 = t24 & t52;

    t89 = mySimplify(t89)
    signals.append(t89)
    t90 = t88 ^ t89;

    t90 = mySimplify(t90)
    signals.append(t90)
    t91 = t23 & t53;

    t91 = mySimplify(t91)
    signals.append(t91)
    t92 = t91 ^ r1_80_18317;

    t92 = mySimplify(t92)
    signals.append(t92)
    t93 = t22 & t53;

    t93 = mySimplify(t93)
    signals.append(t93)
    t94 = t92 ^ t93;

    t94 = mySimplify(t94)
    signals.append(t94)
    t95 = t23 & t52;

    t95 = mySimplify(t95)
    signals.append(t95)
    t96 = t94 ^ t95;

    t96 = mySimplify(t96)
    signals.append(t96)
    t97 = t24 & t54;

    t97 = mySimplify(t97)
    signals.append(t97)
    t98 = t97 ^ r0_80_18316;

    t98 = mySimplify(t98)
    signals.append(t98)
    t99 = t98 ^ r1_80_18317;

    t99 = mySimplify(t99)
    signals.append(t99)
    t100 = t23 & t54;

    t100 = mySimplify(t100)
    signals.append(t100)
    t101 = t99 ^ t100;

    t101 = mySimplify(t101)
    signals.append(t101)
    t102 = t24 & t53;

    t102 = mySimplify(t102)
    signals.append(t102)
    t103 = t101 ^ t102;

    t103 = mySimplify(t103)
    signals.append(t103)
    t104 = t49 & t58;

    t104 = mySimplify(t104)
    signals.append(t104)
    t105 = t104 ^ r0_81_18318;

    t105 = mySimplify(t105)
    signals.append(t105)
    t106 = t49 & t60;

    t106 = mySimplify(t106)
    signals.append(t106)
    t107 = t105 ^ t106;

    t107 = mySimplify(t107)
    signals.append(t107)
    t108 = t51 & t58;

    t108 = mySimplify(t108)
    signals.append(t108)
    t109 = t107 ^ t108;

    t109 = mySimplify(t109)
    signals.append(t109)
    t110 = t50 & t59;

    t110 = mySimplify(t110)
    signals.append(t110)
    t111 = t110 ^ r1_81_18319;

    t111 = mySimplify(t111)
    signals.append(t111)
    t112 = t49 & t59;

    t112 = mySimplify(t112)
    signals.append(t112)
    t113 = t111 ^ t112;

    t113 = mySimplify(t113)
    signals.append(t113)
    t114 = t50 & t58;

    t114 = mySimplify(t114)
    signals.append(t114)
    t115 = t113 ^ t114;

    t115 = mySimplify(t115)
    signals.append(t115)
    t116 = t51 & t60;

    t116 = mySimplify(t116)
    signals.append(t116)
    t117 = t116 ^ r0_81_18318;

    t117 = mySimplify(t117)
    signals.append(t117)
    t118 = t117 ^ r1_81_18319;

    t118 = mySimplify(t118)
    signals.append(t118)
    t119 = t50 & t60;

    t119 = mySimplify(t119)
    signals.append(t119)
    t120 = t118 ^ t119;

    t120 = mySimplify(t120)
    signals.append(t120)
    t121 = t51 & t59;

    t121 = mySimplify(t121)
    signals.append(t121)
    t122 = t120 ^ t121;

    t122 = mySimplify(t122)
    signals.append(t122)
    t123 = t37 & r_18014;

    t123 = mySimplify(t123)
    signals.append(t123)
    t124 = t123 ^ r0_82_18320;

    t124 = mySimplify(t124)
    signals.append(t124)
    t125 = t37 & t15;

    t125 = mySimplify(t125)
    signals.append(t125)
    t126 = t124 ^ t125;

    t126 = mySimplify(t126)
    signals.append(t126)
    t127 = t39 & r_18014;

    t127 = mySimplify(t127)
    signals.append(t127)
    t128 = t126 ^ t127;

    t128 = mySimplify(t128)
    signals.append(t128)
    t129 = t38 & r_18015;

    t129 = mySimplify(t129)
    signals.append(t129)
    t130 = t129 ^ r1_82_18321;

    t130 = mySimplify(t130)
    signals.append(t130)
    t131 = t37 & r_18015;

    t131 = mySimplify(t131)
    signals.append(t131)
    t132 = t130 ^ t131;

    t132 = mySimplify(t132)
    signals.append(t132)
    t133 = t38 & r_18014;

    t133 = mySimplify(t133)
    signals.append(t133)
    t134 = t132 ^ t133;

    t134 = mySimplify(t134)
    signals.append(t134)
    t135 = t39 & t15;

    t135 = mySimplify(t135)
    signals.append(t135)
    t136 = t135 ^ r0_82_18320;

    t136 = mySimplify(t136)
    signals.append(t136)
    t137 = t136 ^ r1_82_18321;

    t137 = mySimplify(t137)
    signals.append(t137)
    t138 = t38 & t15;

    t138 = mySimplify(t138)
    signals.append(t138)
    t139 = t137 ^ t138;

    t139 = mySimplify(t139)
    signals.append(t139)
    t140 = t39 & r_18015;

    t140 = mySimplify(t140)
    signals.append(t140)
    t141 = t139 ^ t140;

    t141 = mySimplify(t141)
    signals.append(t141)
    t142 = t19 & t76;

    t142 = mySimplify(t142)
    signals.append(t142)
    t143 = t142 ^ r0_83_18322;

    t143 = mySimplify(t143)
    signals.append(t143)
    t144 = t19 & t78;

    t144 = mySimplify(t144)
    signals.append(t144)
    t145 = t143 ^ t144;

    t145 = mySimplify(t145)
    signals.append(t145)
    t146 = t21 & t76;

    t146 = mySimplify(t146)
    signals.append(t146)
    t147 = t145 ^ t146;

    t147 = mySimplify(t147)
    signals.append(t147)
    t148 = t20 & t77;

    t148 = mySimplify(t148)
    signals.append(t148)
    t149 = t148 ^ r1_83_18323;

    t149 = mySimplify(t149)
    signals.append(t149)
    t150 = t19 & t77;

    t150 = mySimplify(t150)
    signals.append(t150)
    t151 = t149 ^ t150;

    t151 = mySimplify(t151)
    signals.append(t151)
    t152 = t20 & t76;

    t152 = mySimplify(t152)
    signals.append(t152)
    t153 = t151 ^ t152;

    t153 = mySimplify(t153)
    signals.append(t153)
    t154 = t21 & t78;

    t154 = mySimplify(t154)
    signals.append(t154)
    t155 = t154 ^ r0_83_18322;

    t155 = mySimplify(t155)
    signals.append(t155)
    t156 = t155 ^ r1_83_18323;

    t156 = mySimplify(t156)
    signals.append(t156)
    t157 = t20 & t78;

    t157 = mySimplify(t157)
    signals.append(t157)
    t158 = t156 ^ t157;

    t158 = mySimplify(t158)
    signals.append(t158)
    t159 = t21 & t77;

    t159 = mySimplify(t159)
    signals.append(t159)
    t160 = t158 ^ t159;

    t160 = mySimplify(t160)
    signals.append(t160)
    t161 = t43 & t34;

    t161 = mySimplify(t161)
    signals.append(t161)
    t162 = t161 ^ r0_84_18324;

    t162 = mySimplify(t162)
    signals.append(t162)
    t163 = t43 & t36;

    t163 = mySimplify(t163)
    signals.append(t163)
    t164 = t162 ^ t163;

    t164 = mySimplify(t164)
    signals.append(t164)
    t165 = t45 & t34;

    t165 = mySimplify(t165)
    signals.append(t165)
    t166 = t164 ^ t165;

    t166 = mySimplify(t166)
    signals.append(t166)
    t167 = t44 & t35;

    t167 = mySimplify(t167)
    signals.append(t167)
    t168 = t167 ^ r1_84_18325;

    t168 = mySimplify(t168)
    signals.append(t168)
    t169 = t43 & t35;

    t169 = mySimplify(t169)
    signals.append(t169)
    t170 = t168 ^ t169;

    t170 = mySimplify(t170)
    signals.append(t170)
    t171 = t44 & t34;

    t171 = mySimplify(t171)
    signals.append(t171)
    t172 = t170 ^ t171;

    t172 = mySimplify(t172)
    signals.append(t172)
    t173 = t45 & t36;

    t173 = mySimplify(t173)
    signals.append(t173)
    t174 = t173 ^ r0_84_18324;

    t174 = mySimplify(t174)
    signals.append(t174)
    t175 = t174 ^ r1_84_18325;

    t175 = mySimplify(t175)
    signals.append(t175)
    t176 = t44 & t36;

    t176 = mySimplify(t176)
    signals.append(t176)
    t177 = t175 ^ t176;

    t177 = mySimplify(t177)
    signals.append(t177)
    t178 = t45 & t35;

    t178 = mySimplify(t178)
    signals.append(t178)
    t179 = t177 ^ t178;

    t179 = mySimplify(t179)
    signals.append(t179)
    t180 = t40 & t67;

    t180 = mySimplify(t180)
    signals.append(t180)
    t181 = t180 ^ r0_85_18326;

    t181 = mySimplify(t181)
    signals.append(t181)
    t182 = t40 & t69;

    t182 = mySimplify(t182)
    signals.append(t182)
    t183 = t181 ^ t182;

    t183 = mySimplify(t183)
    signals.append(t183)
    t184 = t42 & t67;

    t184 = mySimplify(t184)
    signals.append(t184)
    t185 = t183 ^ t184;

    t185 = mySimplify(t185)
    signals.append(t185)
    t186 = t41 & t68;

    t186 = mySimplify(t186)
    signals.append(t186)
    t187 = t186 ^ r1_85_18327;

    t187 = mySimplify(t187)
    signals.append(t187)
    t188 = t40 & t68;

    t188 = mySimplify(t188)
    signals.append(t188)
    t189 = t187 ^ t188;

    t189 = mySimplify(t189)
    signals.append(t189)
    t190 = t41 & t67;

    t190 = mySimplify(t190)
    signals.append(t190)
    t191 = t189 ^ t190;

    t191 = mySimplify(t191)
    signals.append(t191)
    t192 = t42 & t69;

    t192 = mySimplify(t192)
    signals.append(t192)
    t193 = t192 ^ r0_85_18326;

    t193 = mySimplify(t193)
    signals.append(t193)
    t194 = t193 ^ r1_85_18327;

    t194 = mySimplify(t194)
    signals.append(t194)
    t195 = t41 & t69;

    t195 = mySimplify(t195)
    signals.append(t195)
    t196 = t194 ^ t195;

    t196 = mySimplify(t196)
    signals.append(t196)
    t197 = t42 & t68;

    t197 = mySimplify(t197)
    signals.append(t197)
    t198 = t196 ^ t197;

    t198 = mySimplify(t198)
    signals.append(t198)
    t199 = t25 & t64;

    t199 = mySimplify(t199)
    signals.append(t199)
    t200 = t199 ^ r0_86_18328;

    t200 = mySimplify(t200)
    signals.append(t200)
    t201 = t25 & t66;

    t201 = mySimplify(t201)
    signals.append(t201)
    t202 = t200 ^ t201;

    t202 = mySimplify(t202)
    signals.append(t202)
    t203 = t27 & t64;

    t203 = mySimplify(t203)
    signals.append(t203)
    t204 = t202 ^ t203;

    t204 = mySimplify(t204)
    signals.append(t204)
    t205 = t26 & t65;

    t205 = mySimplify(t205)
    signals.append(t205)
    t206 = t205 ^ r1_86_18329;

    t206 = mySimplify(t206)
    signals.append(t206)
    t207 = t25 & t65;

    t207 = mySimplify(t207)
    signals.append(t207)
    t208 = t206 ^ t207;

    t208 = mySimplify(t208)
    signals.append(t208)
    t209 = t26 & t64;

    t209 = mySimplify(t209)
    signals.append(t209)
    t210 = t208 ^ t209;

    t210 = mySimplify(t210)
    signals.append(t210)
    t211 = t27 & t66;

    t211 = mySimplify(t211)
    signals.append(t211)
    t212 = t211 ^ r0_86_18328;

    t212 = mySimplify(t212)
    signals.append(t212)
    t213 = t212 ^ r1_86_18329;

    t213 = mySimplify(t213)
    signals.append(t213)
    t214 = t26 & t66;

    t214 = mySimplify(t214)
    signals.append(t214)
    t215 = t213 ^ t214;

    t215 = mySimplify(t215)
    signals.append(t215)
    t216 = t27 & t65;

    t216 = mySimplify(t216)
    signals.append(t216)
    t217 = t215 ^ t216;

    t217 = mySimplify(t217)
    signals.append(t217)
    t218 = t16 & t70;

    t218 = mySimplify(t218)
    signals.append(t218)
    t219 = t218 ^ r0_87_18330;

    t219 = mySimplify(t219)
    signals.append(t219)
    t220 = t16 & t72;

    t220 = mySimplify(t220)
    signals.append(t220)
    t221 = t219 ^ t220;

    t221 = mySimplify(t221)
    signals.append(t221)
    t222 = t18 & t70;

    t222 = mySimplify(t222)
    signals.append(t222)
    t223 = t221 ^ t222;

    t223 = mySimplify(t223)
    signals.append(t223)
    t224 = t17 & t71;

    t224 = mySimplify(t224)
    signals.append(t224)
    t225 = t224 ^ r1_87_18331;

    t225 = mySimplify(t225)
    signals.append(t225)
    t226 = t16 & t71;

    t226 = mySimplify(t226)
    signals.append(t226)
    t227 = t225 ^ t226;

    t227 = mySimplify(t227)
    signals.append(t227)
    t228 = t17 & t70;

    t228 = mySimplify(t228)
    signals.append(t228)
    t229 = t227 ^ t228;

    t229 = mySimplify(t229)
    signals.append(t229)
    t230 = t18 & t72;

    t230 = mySimplify(t230)
    signals.append(t230)
    t231 = t230 ^ r0_87_18330;

    t231 = mySimplify(t231)
    signals.append(t231)
    t232 = t231 ^ r1_87_18331;

    t232 = mySimplify(t232)
    signals.append(t232)
    t233 = t17 & t72;

    t233 = mySimplify(t233)
    signals.append(t233)
    t234 = t232 ^ t233;

    t234 = mySimplify(t234)
    signals.append(t234)
    t235 = t18 & t71;

    t235 = mySimplify(t235)
    signals.append(t235)
    t236 = t234 ^ t235;

    t236 = mySimplify(t236)
    signals.append(t236)
    t237 = t109 ^ t90;

    t237 = mySimplify(t237)
    signals.append(t237)
    t238 = t115 ^ t96;

    t238 = mySimplify(t238)
    signals.append(t238)
    t239 = t122 ^ t103;

    t239 = mySimplify(t239)
    signals.append(t239)
    t240 = t128 ^ t90;

    t240 = mySimplify(t240)
    signals.append(t240)
    t241 = t134 ^ t96;

    t241 = mySimplify(t241)
    signals.append(t241)
    t242 = t141 ^ t103;

    t242 = mySimplify(t242)
    signals.append(t242)
    t243 = t166 ^ t147;

    t243 = mySimplify(t243)
    signals.append(t243)
    t244 = t172 ^ t153;

    t244 = mySimplify(t244)
    signals.append(t244)
    t245 = t179 ^ t160;

    t245 = mySimplify(t245)
    signals.append(t245)
    t246 = t185 ^ t147;

    t246 = mySimplify(t246)
    signals.append(t246)
    t247 = t191 ^ t153;

    t247 = mySimplify(t247)
    signals.append(t247)
    t248 = t198 ^ t160;

    t248 = mySimplify(t248)
    signals.append(t248)
    t249 = t223 ^ t204;

    t249 = mySimplify(t249)
    signals.append(t249)
    t250 = t229 ^ t210;

    t250 = mySimplify(t250)
    signals.append(t250)
    t251 = t236 ^ t217;

    t251 = mySimplify(t251)
    signals.append(t251)
    t252 = t237 ^ t249;

    t252 = mySimplify(t252)
    signals.append(t252)
    t253 = t238 ^ t250;

    t253 = mySimplify(t253)
    signals.append(t253)
    t254 = t239 ^ t251;

    t254 = mySimplify(t254)
    signals.append(t254)
    t255 = t243 ^ t249;

    t255 = mySimplify(t255)
    signals.append(t255)
    t256 = t244 ^ t250;

    t256 = mySimplify(t256)
    signals.append(t256)
    t257 = t245 ^ t251;

    t257 = mySimplify(t257)
    signals.append(t257)
    t258 = t252 ^ t55;

    t258 = mySimplify(t258)
    signals.append(t258)
    t259 = t253 ^ t56;

    t259 = mySimplify(t259)
    signals.append(t259)
    t260 = t254 ^ t57;

    t260 = mySimplify(t260)
    signals.append(t260)
    t261 = t255 ^ t79;

    t261 = mySimplify(t261)
    signals.append(t261)
    t262 = t256 ^ t80;

    t262 = mySimplify(t262)
    signals.append(t262)
    t263 = t257 ^ t81;

    t263 = mySimplify(t263)
    signals.append(t263)
    t264 = t28 & t61;

    t264 = mySimplify(t264)
    signals.append(t264)
    t265 = t264 ^ r0_97_18332;

    t265 = mySimplify(t265)
    signals.append(t265)
    t266 = t28 & t63;

    t266 = mySimplify(t266)
    signals.append(t266)
    t267 = t265 ^ t266;

    t267 = mySimplify(t267)
    signals.append(t267)
    t268 = t30 & t61;

    t268 = mySimplify(t268)
    signals.append(t268)
    t269 = t267 ^ t268;

    t269 = mySimplify(t269)
    signals.append(t269)
    t270 = t29 & t62;

    t270 = mySimplify(t270)
    signals.append(t270)
    t271 = t270 ^ r1_97_18333;

    t271 = mySimplify(t271)
    signals.append(t271)
    t272 = t28 & t62;

    t272 = mySimplify(t272)
    signals.append(t272)
    t273 = t271 ^ t272;

    t273 = mySimplify(t273)
    signals.append(t273)
    t274 = t29 & t61;

    t274 = mySimplify(t274)
    signals.append(t274)
    t275 = t273 ^ t274;

    t275 = mySimplify(t275)
    signals.append(t275)
    t276 = t30 & t63;

    t276 = mySimplify(t276)
    signals.append(t276)
    t277 = t276 ^ r0_97_18332;

    t277 = mySimplify(t277)
    signals.append(t277)
    t278 = t277 ^ r1_97_18333;

    t278 = mySimplify(t278)
    signals.append(t278)
    t279 = t29 & t63;

    t279 = mySimplify(t279)
    signals.append(t279)
    t280 = t278 ^ t279;

    t280 = mySimplify(t280)
    signals.append(t280)
    t281 = t30 & t62;

    t281 = mySimplify(t281)
    signals.append(t281)
    t282 = t280 ^ t281;

    t282 = mySimplify(t282)
    signals.append(t282)
    t283 = t258 & t261;

    t283 = mySimplify(t283)
    signals.append(t283)
    t284 = t283 ^ r0_98_18334;

    t284 = mySimplify(t284)
    signals.append(t284)
    t285 = t258 & t263;

    t285 = mySimplify(t285)
    signals.append(t285)
    t286 = t284 ^ t285;

    t286 = mySimplify(t286)
    signals.append(t286)
    t287 = t260 & t261;

    t287 = mySimplify(t287)
    signals.append(t287)
    t288 = t286 ^ t287;

    t288 = mySimplify(t288)
    signals.append(t288)
    t289 = t259 & t262;

    t289 = mySimplify(t289)
    signals.append(t289)
    t290 = t289 ^ r1_98_18335;

    t290 = mySimplify(t290)
    signals.append(t290)
    t291 = t258 & t262;

    t291 = mySimplify(t291)
    signals.append(t291)
    t292 = t290 ^ t291;

    t292 = mySimplify(t292)
    signals.append(t292)
    t293 = t259 & t261;

    t293 = mySimplify(t293)
    signals.append(t293)
    t294 = t292 ^ t293;

    t294 = mySimplify(t294)
    signals.append(t294)
    t295 = t260 & t263;

    t295 = mySimplify(t295)
    signals.append(t295)
    t296 = t295 ^ r0_98_18334;

    t296 = mySimplify(t296)
    signals.append(t296)
    t297 = t296 ^ r1_98_18335;

    t297 = mySimplify(t297)
    signals.append(t297)
    t298 = t259 & t263;

    t298 = mySimplify(t298)
    signals.append(t298)
    t299 = t297 ^ t298;

    t299 = mySimplify(t299)
    signals.append(t299)
    t300 = t260 & t262;

    t300 = mySimplify(t300)
    signals.append(t300)
    t301 = t299 ^ t300;

    t301 = mySimplify(t301)
    signals.append(t301)
    t302 = t269 ^ t204;

    t302 = mySimplify(t302)
    signals.append(t302)
    t303 = t275 ^ t210;

    t303 = mySimplify(t303)
    signals.append(t303)
    t304 = t282 ^ t217;

    t304 = mySimplify(t304)
    signals.append(t304)
    t305 = t240 ^ t302;

    t305 = mySimplify(t305)
    signals.append(t305)
    t306 = t241 ^ t303;

    t306 = mySimplify(t306)
    signals.append(t306)
    t307 = t242 ^ t304;

    t307 = mySimplify(t307)
    signals.append(t307)
    t308 = t246 ^ t302;

    t308 = mySimplify(t308)
    signals.append(t308)
    t309 = t247 ^ t303;

    t309 = mySimplify(t309)
    signals.append(t309)
    t310 = t248 ^ t304;

    t310 = mySimplify(t310)
    signals.append(t310)
    t311 = t308 ^ t82;

    t311 = mySimplify(t311)
    signals.append(t311)
    t312 = t309 ^ t83;

    t312 = mySimplify(t312)
    signals.append(t312)
    t313 = t310 ^ t84;

    t313 = mySimplify(t313)
    signals.append(t313)
    t314 = t261 ^ t311;

    t314 = mySimplify(t314)
    signals.append(t314)
    t315 = t262 ^ t312;

    t315 = mySimplify(t315)
    signals.append(t315)
    t316 = t263 ^ t313;

    t316 = mySimplify(t316)
    signals.append(t316)
    t317 = t305 ^ t73;

    t317 = mySimplify(t317)
    signals.append(t317)
    t318 = t306 ^ t74;

    t318 = mySimplify(t318)
    signals.append(t318)
    t319 = t307 ^ t75;

    t319 = mySimplify(t319)
    signals.append(t319)
    t320 = t258 ^ t317;

    t320 = mySimplify(t320)
    signals.append(t320)
    t321 = t259 ^ t318;

    t321 = mySimplify(t321)
    signals.append(t321)
    t322 = t260 ^ t319;

    t322 = mySimplify(t322)
    signals.append(t322)
    t323 = t311 ^ t288;

    t323 = mySimplify(t323)
    signals.append(t323)
    t324 = t312 ^ t294;

    t324 = mySimplify(t324)
    signals.append(t324)
    t325 = t313 ^ t301;

    t325 = mySimplify(t325)
    signals.append(t325)
    t326 = t317 ^ t288;

    t326 = mySimplify(t326)
    signals.append(t326)
    t327 = t318 ^ t294;

    t327 = mySimplify(t327)
    signals.append(t327)
    t328 = t319 ^ t301;

    t328 = mySimplify(t328)
    signals.append(t328)
    t329 = t320 & t323;

    t329 = mySimplify(t329)
    signals.append(t329)
    t330 = t329 ^ r0_108_18336;

    t330 = mySimplify(t330)
    signals.append(t330)
    t331 = t320 & t325;

    t331 = mySimplify(t331)
    signals.append(t331)
    t332 = t330 ^ t331;

    t332 = mySimplify(t332)
    signals.append(t332)
    t333 = t322 & t323;

    t333 = mySimplify(t333)
    signals.append(t333)
    t334 = t332 ^ t333;

    t334 = mySimplify(t334)
    signals.append(t334)
    t335 = t321 & t324;

    t335 = mySimplify(t335)
    signals.append(t335)
    t336 = t335 ^ r1_108_18337;

    t336 = mySimplify(t336)
    signals.append(t336)
    t337 = t320 & t324;

    t337 = mySimplify(t337)
    signals.append(t337)
    t338 = t336 ^ t337;

    t338 = mySimplify(t338)
    signals.append(t338)
    t339 = t321 & t323;

    t339 = mySimplify(t339)
    signals.append(t339)
    t340 = t338 ^ t339;

    t340 = mySimplify(t340)
    signals.append(t340)
    t341 = t322 & t325;

    t341 = mySimplify(t341)
    signals.append(t341)
    t342 = t341 ^ r0_108_18336;

    t342 = mySimplify(t342)
    signals.append(t342)
    t343 = t342 ^ r1_108_18337;

    t343 = mySimplify(t343)
    signals.append(t343)
    t344 = t321 & t325;

    t344 = mySimplify(t344)
    signals.append(t344)
    t345 = t343 ^ t344;

    t345 = mySimplify(t345)
    signals.append(t345)
    t346 = t322 & t324;

    t346 = mySimplify(t346)
    signals.append(t346)
    t347 = t345 ^ t346;

    t347 = mySimplify(t347)
    signals.append(t347)
    t348 = t326 & t314;

    t348 = mySimplify(t348)
    signals.append(t348)
    t349 = t348 ^ r0_109_18338;

    t349 = mySimplify(t349)
    signals.append(t349)
    t350 = t326 & t316;

    t350 = mySimplify(t350)
    signals.append(t350)
    t351 = t349 ^ t350;

    t351 = mySimplify(t351)
    signals.append(t351)
    t352 = t328 & t314;

    t352 = mySimplify(t352)
    signals.append(t352)
    t353 = t351 ^ t352;

    t353 = mySimplify(t353)
    signals.append(t353)
    t354 = t327 & t315;

    t354 = mySimplify(t354)
    signals.append(t354)
    t355 = t354 ^ r1_109_18339;

    t355 = mySimplify(t355)
    signals.append(t355)
    t356 = t326 & t315;

    t356 = mySimplify(t356)
    signals.append(t356)
    t357 = t355 ^ t356;

    t357 = mySimplify(t357)
    signals.append(t357)
    t358 = t327 & t314;

    t358 = mySimplify(t358)
    signals.append(t358)
    t359 = t357 ^ t358;

    t359 = mySimplify(t359)
    signals.append(t359)
    t360 = t328 & t316;

    t360 = mySimplify(t360)
    signals.append(t360)
    t361 = t360 ^ r0_109_18338;

    t361 = mySimplify(t361)
    signals.append(t361)
    t362 = t361 ^ r1_109_18339;

    t362 = mySimplify(t362)
    signals.append(t362)
    t363 = t327 & t316;

    t363 = mySimplify(t363)
    signals.append(t363)
    t364 = t362 ^ t363;

    t364 = mySimplify(t364)
    signals.append(t364)
    t365 = t328 & t315;

    t365 = mySimplify(t365)
    signals.append(t365)
    t366 = t364 ^ t365;

    t366 = mySimplify(t366)
    signals.append(t366)
    t367 = t334 ^ t317;

    t367 = mySimplify(t367)
    signals.append(t367)
    t368 = t340 ^ t318;

    t368 = mySimplify(t368)
    signals.append(t368)
    t369 = t347 ^ t319;

    t369 = mySimplify(t369)
    signals.append(t369)
    t370 = t353 ^ t311;

    t370 = mySimplify(t370)
    signals.append(t370)
    t371 = t359 ^ t312;

    t371 = mySimplify(t371)
    signals.append(t371)
    t372 = t366 ^ t313;

    t372 = mySimplify(t372)
    signals.append(t372)
    t373 = t261 ^ t370;

    t373 = mySimplify(t373)
    signals.append(t373)
    t374 = t262 ^ t371;

    t374 = mySimplify(t374)
    signals.append(t374)
    t375 = t263 ^ t372;

    t375 = mySimplify(t375)
    signals.append(t375)
    t376 = t323 ^ t370;

    t376 = mySimplify(t376)
    signals.append(t376)
    t377 = t324 ^ t371;

    t377 = mySimplify(t377)
    signals.append(t377)
    t378 = t325 ^ t372;

    t378 = mySimplify(t378)
    signals.append(t378)
    t379 = t367 ^ t370;

    t379 = mySimplify(t379)
    signals.append(t379)
    t380 = t368 ^ t371;

    t380 = mySimplify(t380)
    signals.append(t380)
    t381 = t369 ^ t372;

    t381 = mySimplify(t381)
    signals.append(t381)
    t382 = t367 & t40;

    t382 = mySimplify(t382)
    signals.append(t382)
    t383 = t382 ^ r0_115_18340;

    t383 = mySimplify(t383)
    signals.append(t383)
    t384 = t367 & t42;

    t384 = mySimplify(t384)
    signals.append(t384)
    t385 = t383 ^ t384;

    t385 = mySimplify(t385)
    signals.append(t385)
    t386 = t369 & t40;

    t386 = mySimplify(t386)
    signals.append(t386)
    t387 = t385 ^ t386;

    t387 = mySimplify(t387)
    signals.append(t387)
    t388 = t368 & t41;

    t388 = mySimplify(t388)
    signals.append(t388)
    t389 = t388 ^ r1_115_18341;

    t389 = mySimplify(t389)
    signals.append(t389)
    t390 = t367 & t41;

    t390 = mySimplify(t390)
    signals.append(t390)
    t391 = t389 ^ t390;

    t391 = mySimplify(t391)
    signals.append(t391)
    t392 = t368 & t40;

    t392 = mySimplify(t392)
    signals.append(t392)
    t393 = t391 ^ t392;

    t393 = mySimplify(t393)
    signals.append(t393)
    t394 = t369 & t42;

    t394 = mySimplify(t394)
    signals.append(t394)
    t395 = t394 ^ r0_115_18340;

    t395 = mySimplify(t395)
    signals.append(t395)
    t396 = t395 ^ r1_115_18341;

    t396 = mySimplify(t396)
    signals.append(t396)
    t397 = t368 & t42;

    t397 = mySimplify(t397)
    signals.append(t397)
    t398 = t396 ^ t397;

    t398 = mySimplify(t398)
    signals.append(t398)
    t399 = t369 & t41;

    t399 = mySimplify(t399)
    signals.append(t399)
    t400 = t398 ^ t399;

    t400 = mySimplify(t400)
    signals.append(t400)
    t401 = t311 & t376;

    t401 = mySimplify(t401)
    signals.append(t401)
    t402 = t401 ^ r0_116_18342;

    t402 = mySimplify(t402)
    signals.append(t402)
    t403 = t311 & t378;

    t403 = mySimplify(t403)
    signals.append(t403)
    t404 = t402 ^ t403;

    t404 = mySimplify(t404)
    signals.append(t404)
    t405 = t313 & t376;

    t405 = mySimplify(t405)
    signals.append(t405)
    t406 = t404 ^ t405;

    t406 = mySimplify(t406)
    signals.append(t406)
    t407 = t312 & t377;

    t407 = mySimplify(t407)
    signals.append(t407)
    t408 = t407 ^ r1_116_18343;

    t408 = mySimplify(t408)
    signals.append(t408)
    t409 = t311 & t377;

    t409 = mySimplify(t409)
    signals.append(t409)
    t410 = t408 ^ t409;

    t410 = mySimplify(t410)
    signals.append(t410)
    t411 = t312 & t376;

    t411 = mySimplify(t411)
    signals.append(t411)
    t412 = t410 ^ t411;

    t412 = mySimplify(t412)
    signals.append(t412)
    t413 = t313 & t378;

    t413 = mySimplify(t413)
    signals.append(t413)
    t414 = t413 ^ r0_116_18342;

    t414 = mySimplify(t414)
    signals.append(t414)
    t415 = t414 ^ r1_116_18343;

    t415 = mySimplify(t415)
    signals.append(t415)
    t416 = t312 & t378;

    t416 = mySimplify(t416)
    signals.append(t416)
    t417 = t415 ^ t416;

    t417 = mySimplify(t417)
    signals.append(t417)
    t418 = t313 & t377;

    t418 = mySimplify(t418)
    signals.append(t418)
    t419 = t417 ^ t418;

    t419 = mySimplify(t419)
    signals.append(t419)
    t420 = t406 ^ t373;

    t420 = mySimplify(t420)
    signals.append(t420)
    t421 = t412 ^ t374;

    t421 = mySimplify(t421)
    signals.append(t421)
    t422 = t419 ^ t375;

    t422 = mySimplify(t422)
    signals.append(t422)
    t423 = t323 ^ t406;

    t423 = mySimplify(t423)
    signals.append(t423)
    t424 = t324 ^ t412;

    t424 = mySimplify(t424)
    signals.append(t424)
    t425 = t325 ^ t419;

    t425 = mySimplify(t425)
    signals.append(t425)
    t426 = t367 & t423;

    t426 = mySimplify(t426)
    signals.append(t426)
    t427 = t426 ^ r0_119_18344;

    t427 = mySimplify(t427)
    signals.append(t427)
    t428 = t367 & t425;

    t428 = mySimplify(t428)
    signals.append(t428)
    t429 = t427 ^ t428;

    t429 = mySimplify(t429)
    signals.append(t429)
    t430 = t369 & t423;

    t430 = mySimplify(t430)
    signals.append(t430)
    t431 = t429 ^ t430;

    t431 = mySimplify(t431)
    signals.append(t431)
    t432 = t368 & t424;

    t432 = mySimplify(t432)
    signals.append(t432)
    t433 = t432 ^ r1_119_18345;

    t433 = mySimplify(t433)
    signals.append(t433)
    t434 = t367 & t424;

    t434 = mySimplify(t434)
    signals.append(t434)
    t435 = t433 ^ t434;

    t435 = mySimplify(t435)
    signals.append(t435)
    t436 = t368 & t423;

    t436 = mySimplify(t436)
    signals.append(t436)
    t437 = t435 ^ t436;

    t437 = mySimplify(t437)
    signals.append(t437)
    t438 = t369 & t425;

    t438 = mySimplify(t438)
    signals.append(t438)
    t439 = t438 ^ r0_119_18344;

    t439 = mySimplify(t439)
    signals.append(t439)
    t440 = t439 ^ r1_119_18345;

    t440 = mySimplify(t440)
    signals.append(t440)
    t441 = t368 & t425;

    t441 = mySimplify(t441)
    signals.append(t441)
    t442 = t440 ^ t441;

    t442 = mySimplify(t442)
    signals.append(t442)
    t443 = t369 & t424;

    t443 = mySimplify(t443)
    signals.append(t443)
    t444 = t442 ^ t443;

    t444 = mySimplify(t444)
    signals.append(t444)
    t445 = t367 & t67;

    t445 = mySimplify(t445)
    signals.append(t445)
    t446 = t445 ^ r0_120_18346;

    t446 = mySimplify(t446)
    signals.append(t446)
    t447 = t367 & t69;

    t447 = mySimplify(t447)
    signals.append(t447)
    t448 = t446 ^ t447;

    t448 = mySimplify(t448)
    signals.append(t448)
    t449 = t369 & t67;

    t449 = mySimplify(t449)
    signals.append(t449)
    t450 = t448 ^ t449;

    t450 = mySimplify(t450)
    signals.append(t450)
    t451 = t368 & t68;

    t451 = mySimplify(t451)
    signals.append(t451)
    t452 = t451 ^ r1_120_18347;

    t452 = mySimplify(t452)
    signals.append(t452)
    t453 = t367 & t68;

    t453 = mySimplify(t453)
    signals.append(t453)
    t454 = t452 ^ t453;

    t454 = mySimplify(t454)
    signals.append(t454)
    t455 = t368 & t67;

    t455 = mySimplify(t455)
    signals.append(t455)
    t456 = t454 ^ t455;

    t456 = mySimplify(t456)
    signals.append(t456)
    t457 = t369 & t69;

    t457 = mySimplify(t457)
    signals.append(t457)
    t458 = t457 ^ r0_120_18346;

    t458 = mySimplify(t458)
    signals.append(t458)
    t459 = t458 ^ r1_120_18347;

    t459 = mySimplify(t459)
    signals.append(t459)
    t460 = t368 & t69;

    t460 = mySimplify(t460)
    signals.append(t460)
    t461 = t459 ^ t460;

    t461 = mySimplify(t461)
    signals.append(t461)
    t462 = t369 & t68;

    t462 = mySimplify(t462)
    signals.append(t462)
    t463 = t461 ^ t462;

    t463 = mySimplify(t463)
    signals.append(t463)
    t464 = t370 ^ t420;

    t464 = mySimplify(t464)
    signals.append(t464)
    t465 = t371 ^ t421;

    t465 = mySimplify(t465)
    signals.append(t465)
    t466 = t372 ^ t422;

    t466 = mySimplify(t466)
    signals.append(t466)
    t467 = t320 ^ t431;

    t467 = mySimplify(t467)
    signals.append(t467)
    t468 = t321 ^ t437;

    t468 = mySimplify(t468)
    signals.append(t468)
    t469 = t322 ^ t444;

    t469 = mySimplify(t469)
    signals.append(t469)
    t470 = t467 ^ t420;

    t470 = mySimplify(t470)
    signals.append(t470)
    t471 = t468 ^ t421;

    t471 = mySimplify(t471)
    signals.append(t471)
    t472 = t469 ^ t422;

    t472 = mySimplify(t472)
    signals.append(t472)
    t473 = t367 ^ t467;

    t473 = mySimplify(t473)
    signals.append(t473)
    t474 = t368 ^ t468;

    t474 = mySimplify(t474)
    signals.append(t474)
    t475 = t369 ^ t469;

    t475 = mySimplify(t475)
    signals.append(t475)
    t476 = t379 ^ t470;

    t476 = mySimplify(t476)
    signals.append(t476)
    t477 = t380 ^ t471;

    t477 = mySimplify(t477)
    signals.append(t477)
    t478 = t381 ^ t472;

    t478 = mySimplify(t478)
    signals.append(t478)
    t479 = t464 & t52;

    t479 = mySimplify(t479)
    signals.append(t479)
    t480 = t479 ^ r0_126_18348;

    t480 = mySimplify(t480)
    signals.append(t480)
    t481 = t464 & t54;

    t481 = mySimplify(t481)
    signals.append(t481)
    t482 = t480 ^ t481;

    t482 = mySimplify(t482)
    signals.append(t482)
    t483 = t466 & t52;

    t483 = mySimplify(t483)
    signals.append(t483)
    t484 = t482 ^ t483;

    t484 = mySimplify(t484)
    signals.append(t484)
    t485 = t465 & t53;

    t485 = mySimplify(t485)
    signals.append(t485)
    t486 = t485 ^ r1_126_18349;

    t486 = mySimplify(t486)
    signals.append(t486)
    t487 = t464 & t53;

    t487 = mySimplify(t487)
    signals.append(t487)
    t488 = t486 ^ t487;

    t488 = mySimplify(t488)
    signals.append(t488)
    t489 = t465 & t52;

    t489 = mySimplify(t489)
    signals.append(t489)
    t490 = t488 ^ t489;

    t490 = mySimplify(t490)
    signals.append(t490)
    t491 = t466 & t54;

    t491 = mySimplify(t491)
    signals.append(t491)
    t492 = t491 ^ r0_126_18348;

    t492 = mySimplify(t492)
    signals.append(t492)
    t493 = t492 ^ r1_126_18349;

    t493 = mySimplify(t493)
    signals.append(t493)
    t494 = t465 & t54;

    t494 = mySimplify(t494)
    signals.append(t494)
    t495 = t493 ^ t494;

    t495 = mySimplify(t495)
    signals.append(t495)
    t496 = t466 & t53;

    t496 = mySimplify(t496)
    signals.append(t496)
    t497 = t495 ^ t496;

    t497 = mySimplify(t497)
    signals.append(t497)
    t498 = t420 & t58;

    t498 = mySimplify(t498)
    signals.append(t498)
    t499 = t498 ^ r0_127_18350;

    t499 = mySimplify(t499)
    signals.append(t499)
    t500 = t420 & t60;

    t500 = mySimplify(t500)
    signals.append(t500)
    t501 = t499 ^ t500;

    t501 = mySimplify(t501)
    signals.append(t501)
    t502 = t422 & t58;

    t502 = mySimplify(t502)
    signals.append(t502)
    t503 = t501 ^ t502;

    t503 = mySimplify(t503)
    signals.append(t503)
    t504 = t421 & t59;

    t504 = mySimplify(t504)
    signals.append(t504)
    t505 = t504 ^ r1_127_18351;

    t505 = mySimplify(t505)
    signals.append(t505)
    t506 = t420 & t59;

    t506 = mySimplify(t506)
    signals.append(t506)
    t507 = t505 ^ t506;

    t507 = mySimplify(t507)
    signals.append(t507)
    t508 = t421 & t58;

    t508 = mySimplify(t508)
    signals.append(t508)
    t509 = t507 ^ t508;

    t509 = mySimplify(t509)
    signals.append(t509)
    t510 = t422 & t60;

    t510 = mySimplify(t510)
    signals.append(t510)
    t511 = t510 ^ r0_127_18350;

    t511 = mySimplify(t511)
    signals.append(t511)
    t512 = t511 ^ r1_127_18351;

    t512 = mySimplify(t512)
    signals.append(t512)
    t513 = t421 & t60;

    t513 = mySimplify(t513)
    signals.append(t513)
    t514 = t512 ^ t513;

    t514 = mySimplify(t514)
    signals.append(t514)
    t515 = t422 & t59;

    t515 = mySimplify(t515)
    signals.append(t515)
    t516 = t514 ^ t515;

    t516 = mySimplify(t516)
    signals.append(t516)
    t517 = t464 & t22;

    t517 = mySimplify(t517)
    signals.append(t517)
    t518 = t517 ^ r0_128_18352;

    t518 = mySimplify(t518)
    signals.append(t518)
    t519 = t464 & t24;

    t519 = mySimplify(t519)
    signals.append(t519)
    t520 = t518 ^ t519;

    t520 = mySimplify(t520)
    signals.append(t520)
    t521 = t466 & t22;

    t521 = mySimplify(t521)
    signals.append(t521)
    t522 = t520 ^ t521;

    t522 = mySimplify(t522)
    signals.append(t522)
    t523 = t465 & t23;

    t523 = mySimplify(t523)
    signals.append(t523)
    t524 = t523 ^ r1_128_18353;

    t524 = mySimplify(t524)
    signals.append(t524)
    t525 = t464 & t23;

    t525 = mySimplify(t525)
    signals.append(t525)
    t526 = t524 ^ t525;

    t526 = mySimplify(t526)
    signals.append(t526)
    t527 = t465 & t22;

    t527 = mySimplify(t527)
    signals.append(t527)
    t528 = t526 ^ t527;

    t528 = mySimplify(t528)
    signals.append(t528)
    t529 = t466 & t24;

    t529 = mySimplify(t529)
    signals.append(t529)
    t530 = t529 ^ r0_128_18352;

    t530 = mySimplify(t530)
    signals.append(t530)
    t531 = t530 ^ r1_128_18353;

    t531 = mySimplify(t531)
    signals.append(t531)
    t532 = t465 & t24;

    t532 = mySimplify(t532)
    signals.append(t532)
    t533 = t531 ^ t532;

    t533 = mySimplify(t533)
    signals.append(t533)
    t534 = t466 & t23;

    t534 = mySimplify(t534)
    signals.append(t534)
    t535 = t533 ^ t534;

    t535 = mySimplify(t535)
    signals.append(t535)
    t536 = t420 & t49;

    t536 = mySimplify(t536)
    signals.append(t536)
    t537 = t536 ^ r0_129_18354;

    t537 = mySimplify(t537)
    signals.append(t537)
    t538 = t420 & t51;

    t538 = mySimplify(t538)
    signals.append(t538)
    t539 = t537 ^ t538;

    t539 = mySimplify(t539)
    signals.append(t539)
    t540 = t422 & t49;

    t540 = mySimplify(t540)
    signals.append(t540)
    t541 = t539 ^ t540;

    t541 = mySimplify(t541)
    signals.append(t541)
    t542 = t421 & t50;

    t542 = mySimplify(t542)
    signals.append(t542)
    t543 = t542 ^ r1_129_18355;

    t543 = mySimplify(t543)
    signals.append(t543)
    t544 = t420 & t50;

    t544 = mySimplify(t544)
    signals.append(t544)
    t545 = t543 ^ t544;

    t545 = mySimplify(t545)
    signals.append(t545)
    t546 = t421 & t49;

    t546 = mySimplify(t546)
    signals.append(t546)
    t547 = t545 ^ t546;

    t547 = mySimplify(t547)
    signals.append(t547)
    t548 = t422 & t51;

    t548 = mySimplify(t548)
    signals.append(t548)
    t549 = t548 ^ r0_129_18354;

    t549 = mySimplify(t549)
    signals.append(t549)
    t550 = t549 ^ r1_129_18355;

    t550 = mySimplify(t550)
    signals.append(t550)
    t551 = t421 & t51;

    t551 = mySimplify(t551)
    signals.append(t551)
    t552 = t550 ^ t551;

    t552 = mySimplify(t552)
    signals.append(t552)
    t553 = t422 & t50;

    t553 = mySimplify(t553)
    signals.append(t553)
    t554 = t552 ^ t553;

    t554 = mySimplify(t554)
    signals.append(t554)
    t555 = t467 & t34;

    t555 = mySimplify(t555)
    signals.append(t555)
    t556 = t555 ^ r0_130_18356;

    t556 = mySimplify(t556)
    signals.append(t556)
    t557 = t467 & t36;

    t557 = mySimplify(t557)
    signals.append(t557)
    t558 = t556 ^ t557;

    t558 = mySimplify(t558)
    signals.append(t558)
    t559 = t469 & t34;

    t559 = mySimplify(t559)
    signals.append(t559)
    t560 = t558 ^ t559;

    t560 = mySimplify(t560)
    signals.append(t560)
    t561 = t468 & t35;

    t561 = mySimplify(t561)
    signals.append(t561)
    t562 = t561 ^ r1_130_18357;

    t562 = mySimplify(t562)
    signals.append(t562)
    t563 = t467 & t35;

    t563 = mySimplify(t563)
    signals.append(t563)
    t564 = t562 ^ t563;

    t564 = mySimplify(t564)
    signals.append(t564)
    t565 = t468 & t34;

    t565 = mySimplify(t565)
    signals.append(t565)
    t566 = t564 ^ t565;

    t566 = mySimplify(t566)
    signals.append(t566)
    t567 = t469 & t36;

    t567 = mySimplify(t567)
    signals.append(t567)
    t568 = t567 ^ r0_130_18356;

    t568 = mySimplify(t568)
    signals.append(t568)
    t569 = t568 ^ r1_130_18357;

    t569 = mySimplify(t569)
    signals.append(t569)
    t570 = t468 & t36;

    t570 = mySimplify(t570)
    signals.append(t570)
    t571 = t569 ^ t570;

    t571 = mySimplify(t571)
    signals.append(t571)
    t572 = t469 & t35;

    t572 = mySimplify(t572)
    signals.append(t572)
    t573 = t571 ^ t572;

    t573 = mySimplify(t573)
    signals.append(t573)
    t574 = t379 & t64;

    t574 = mySimplify(t574)
    signals.append(t574)
    t575 = t574 ^ r0_131_18358;

    t575 = mySimplify(t575)
    signals.append(t575)
    t576 = t379 & t66;

    t576 = mySimplify(t576)
    signals.append(t576)
    t577 = t575 ^ t576;

    t577 = mySimplify(t577)
    signals.append(t577)
    t578 = t381 & t64;

    t578 = mySimplify(t578)
    signals.append(t578)
    t579 = t577 ^ t578;

    t579 = mySimplify(t579)
    signals.append(t579)
    t580 = t380 & t65;

    t580 = mySimplify(t580)
    signals.append(t580)
    t581 = t580 ^ r1_131_18359;

    t581 = mySimplify(t581)
    signals.append(t581)
    t582 = t379 & t65;

    t582 = mySimplify(t582)
    signals.append(t582)
    t583 = t581 ^ t582;

    t583 = mySimplify(t583)
    signals.append(t583)
    t584 = t380 & t64;

    t584 = mySimplify(t584)
    signals.append(t584)
    t585 = t583 ^ t584;

    t585 = mySimplify(t585)
    signals.append(t585)
    t586 = t381 & t66;

    t586 = mySimplify(t586)
    signals.append(t586)
    t587 = t586 ^ r0_131_18358;

    t587 = mySimplify(t587)
    signals.append(t587)
    t588 = t587 ^ r1_131_18359;

    t588 = mySimplify(t588)
    signals.append(t588)
    t589 = t380 & t66;

    t589 = mySimplify(t589)
    signals.append(t589)
    t590 = t588 ^ t589;

    t590 = mySimplify(t590)
    signals.append(t590)
    t591 = t381 & t65;

    t591 = mySimplify(t591)
    signals.append(t591)
    t592 = t590 ^ t591;

    t592 = mySimplify(t592)
    signals.append(t592)
    t593 = t467 & t43;

    t593 = mySimplify(t593)
    signals.append(t593)
    t594 = t593 ^ r0_132_18360;

    t594 = mySimplify(t594)
    signals.append(t594)
    t595 = t467 & t45;

    t595 = mySimplify(t595)
    signals.append(t595)
    t596 = t594 ^ t595;

    t596 = mySimplify(t596)
    signals.append(t596)
    t597 = t469 & t43;

    t597 = mySimplify(t597)
    signals.append(t597)
    t598 = t596 ^ t597;

    t598 = mySimplify(t598)
    signals.append(t598)
    t599 = t468 & t44;

    t599 = mySimplify(t599)
    signals.append(t599)
    t600 = t599 ^ r1_132_18361;

    t600 = mySimplify(t600)
    signals.append(t600)
    t601 = t467 & t44;

    t601 = mySimplify(t601)
    signals.append(t601)
    t602 = t600 ^ t601;

    t602 = mySimplify(t602)
    signals.append(t602)
    t603 = t468 & t43;

    t603 = mySimplify(t603)
    signals.append(t603)
    t604 = t602 ^ t603;

    t604 = mySimplify(t604)
    signals.append(t604)
    t605 = t469 & t45;

    t605 = mySimplify(t605)
    signals.append(t605)
    t606 = t605 ^ r0_132_18360;

    t606 = mySimplify(t606)
    signals.append(t606)
    t607 = t606 ^ r1_132_18361;

    t607 = mySimplify(t607)
    signals.append(t607)
    t608 = t468 & t45;

    t608 = mySimplify(t608)
    signals.append(t608)
    t609 = t607 ^ t608;

    t609 = mySimplify(t609)
    signals.append(t609)
    t610 = t469 & t44;

    t610 = mySimplify(t610)
    signals.append(t610)
    t611 = t609 ^ t610;

    t611 = mySimplify(t611)
    signals.append(t611)
    t612 = t379 & t25;

    t612 = mySimplify(t612)
    signals.append(t612)
    t613 = t612 ^ r0_133_18362;

    t613 = mySimplify(t613)
    signals.append(t613)
    t614 = t379 & t27;

    t614 = mySimplify(t614)
    signals.append(t614)
    t615 = t613 ^ t614;

    t615 = mySimplify(t615)
    signals.append(t615)
    t616 = t381 & t25;

    t616 = mySimplify(t616)
    signals.append(t616)
    t617 = t615 ^ t616;

    t617 = mySimplify(t617)
    signals.append(t617)
    t618 = t380 & t26;

    t618 = mySimplify(t618)
    signals.append(t618)
    t619 = t618 ^ r1_133_18363;

    t619 = mySimplify(t619)
    signals.append(t619)
    t620 = t379 & t26;

    t620 = mySimplify(t620)
    signals.append(t620)
    t621 = t619 ^ t620;

    t621 = mySimplify(t621)
    signals.append(t621)
    t622 = t380 & t25;

    t622 = mySimplify(t622)
    signals.append(t622)
    t623 = t621 ^ t622;

    t623 = mySimplify(t623)
    signals.append(t623)
    t624 = t381 & t27;

    t624 = mySimplify(t624)
    signals.append(t624)
    t625 = t624 ^ r0_133_18362;

    t625 = mySimplify(t625)
    signals.append(t625)
    t626 = t625 ^ r1_133_18363;

    t626 = mySimplify(t626)
    signals.append(t626)
    t627 = t380 & t27;

    t627 = mySimplify(t627)
    signals.append(t627)
    t628 = t626 ^ t627;

    t628 = mySimplify(t628)
    signals.append(t628)
    t629 = t381 & t26;

    t629 = mySimplify(t629)
    signals.append(t629)
    t630 = t628 ^ t629;

    t630 = mySimplify(t630)
    signals.append(t630)
    t631 = t476 & t70;

    t631 = mySimplify(t631)
    signals.append(t631)
    t632 = t631 ^ r0_134_18364;

    t632 = mySimplify(t632)
    signals.append(t632)
    t633 = t476 & t72;

    t633 = mySimplify(t633)
    signals.append(t633)
    t634 = t632 ^ t633;

    t634 = mySimplify(t634)
    signals.append(t634)
    t635 = t478 & t70;

    t635 = mySimplify(t635)
    signals.append(t635)
    t636 = t634 ^ t635;

    t636 = mySimplify(t636)
    signals.append(t636)
    t637 = t477 & t71;

    t637 = mySimplify(t637)
    signals.append(t637)
    t638 = t637 ^ r1_134_18365;

    t638 = mySimplify(t638)
    signals.append(t638)
    t639 = t476 & t71;

    t639 = mySimplify(t639)
    signals.append(t639)
    t640 = t638 ^ t639;

    t640 = mySimplify(t640)
    signals.append(t640)
    t641 = t477 & t70;

    t641 = mySimplify(t641)
    signals.append(t641)
    t642 = t640 ^ t641;

    t642 = mySimplify(t642)
    signals.append(t642)
    t643 = t478 & t72;

    t643 = mySimplify(t643)
    signals.append(t643)
    t644 = t643 ^ r0_134_18364;

    t644 = mySimplify(t644)
    signals.append(t644)
    t645 = t644 ^ r1_134_18365;

    t645 = mySimplify(t645)
    signals.append(t645)
    t646 = t477 & t72;

    t646 = mySimplify(t646)
    signals.append(t646)
    t647 = t645 ^ t646;

    t647 = mySimplify(t647)
    signals.append(t647)
    t648 = t478 & t71;

    t648 = mySimplify(t648)
    signals.append(t648)
    t649 = t647 ^ t648;

    t649 = mySimplify(t649)
    signals.append(t649)
    t650 = t470 & t61;

    t650 = mySimplify(t650)
    signals.append(t650)
    t651 = t650 ^ r0_135_18366;

    t651 = mySimplify(t651)
    signals.append(t651)
    t652 = t470 & t63;

    t652 = mySimplify(t652)
    signals.append(t652)
    t653 = t651 ^ t652;

    t653 = mySimplify(t653)
    signals.append(t653)
    t654 = t472 & t61;

    t654 = mySimplify(t654)
    signals.append(t654)
    t655 = t653 ^ t654;

    t655 = mySimplify(t655)
    signals.append(t655)
    t656 = t471 & t62;

    t656 = mySimplify(t656)
    signals.append(t656)
    t657 = t656 ^ r1_135_18367;

    t657 = mySimplify(t657)
    signals.append(t657)
    t658 = t470 & t62;

    t658 = mySimplify(t658)
    signals.append(t658)
    t659 = t657 ^ t658;

    t659 = mySimplify(t659)
    signals.append(t659)
    t660 = t471 & t61;

    t660 = mySimplify(t660)
    signals.append(t660)
    t661 = t659 ^ t660;

    t661 = mySimplify(t661)
    signals.append(t661)
    t662 = t472 & t63;

    t662 = mySimplify(t662)
    signals.append(t662)
    t663 = t662 ^ r0_135_18366;

    t663 = mySimplify(t663)
    signals.append(t663)
    t664 = t663 ^ r1_135_18367;

    t664 = mySimplify(t664)
    signals.append(t664)
    t665 = t471 & t63;

    t665 = mySimplify(t665)
    signals.append(t665)
    t666 = t664 ^ t665;

    t666 = mySimplify(t666)
    signals.append(t666)
    t667 = t472 & t62;

    t667 = mySimplify(t667)
    signals.append(t667)
    t668 = t666 ^ t667;

    t668 = mySimplify(t668)
    signals.append(t668)
    t669 = t476 & t16;

    t669 = mySimplify(t669)
    signals.append(t669)
    t670 = t669 ^ r0_136_18368;

    t670 = mySimplify(t670)
    signals.append(t670)
    t671 = t476 & t18;

    t671 = mySimplify(t671)
    signals.append(t671)
    t672 = t670 ^ t671;

    t672 = mySimplify(t672)
    signals.append(t672)
    t673 = t478 & t16;

    t673 = mySimplify(t673)
    signals.append(t673)
    t674 = t672 ^ t673;

    t674 = mySimplify(t674)
    signals.append(t674)
    t675 = t477 & t17;

    t675 = mySimplify(t675)
    signals.append(t675)
    t676 = t675 ^ r1_136_18369;

    t676 = mySimplify(t676)
    signals.append(t676)
    t677 = t476 & t17;

    t677 = mySimplify(t677)
    signals.append(t677)
    t678 = t676 ^ t677;

    t678 = mySimplify(t678)
    signals.append(t678)
    t679 = t477 & t16;

    t679 = mySimplify(t679)
    signals.append(t679)
    t680 = t678 ^ t679;

    t680 = mySimplify(t680)
    signals.append(t680)
    t681 = t478 & t18;

    t681 = mySimplify(t681)
    signals.append(t681)
    t682 = t681 ^ r0_136_18368;

    t682 = mySimplify(t682)
    signals.append(t682)
    t683 = t682 ^ r1_136_18369;

    t683 = mySimplify(t683)
    signals.append(t683)
    t684 = t477 & t18;

    t684 = mySimplify(t684)
    signals.append(t684)
    t685 = t683 ^ t684;

    t685 = mySimplify(t685)
    signals.append(t685)
    t686 = t478 & t17;

    t686 = mySimplify(t686)
    signals.append(t686)
    t687 = t685 ^ t686;

    t687 = mySimplify(t687)
    signals.append(t687)
    t688 = t470 & t28;

    t688 = mySimplify(t688)
    signals.append(t688)
    t689 = t688 ^ r0_137_18370;

    t689 = mySimplify(t689)
    signals.append(t689)
    t690 = t470 & t30;

    t690 = mySimplify(t690)
    signals.append(t690)
    t691 = t689 ^ t690;

    t691 = mySimplify(t691)
    signals.append(t691)
    t692 = t472 & t28;

    t692 = mySimplify(t692)
    signals.append(t692)
    t693 = t691 ^ t692;

    t693 = mySimplify(t693)
    signals.append(t693)
    t694 = t471 & t29;

    t694 = mySimplify(t694)
    signals.append(t694)
    t695 = t694 ^ r1_137_18371;

    t695 = mySimplify(t695)
    signals.append(t695)
    t696 = t470 & t29;

    t696 = mySimplify(t696)
    signals.append(t696)
    t697 = t695 ^ t696;

    t697 = mySimplify(t697)
    signals.append(t697)
    t698 = t471 & t28;

    t698 = mySimplify(t698)
    signals.append(t698)
    t699 = t697 ^ t698;

    t699 = mySimplify(t699)
    signals.append(t699)
    t700 = t472 & t30;

    t700 = mySimplify(t700)
    signals.append(t700)
    t701 = t700 ^ r0_137_18370;

    t701 = mySimplify(t701)
    signals.append(t701)
    t702 = t701 ^ r1_137_18371;

    t702 = mySimplify(t702)
    signals.append(t702)
    t703 = t471 & t30;

    t703 = mySimplify(t703)
    signals.append(t703)
    t704 = t702 ^ t703;

    t704 = mySimplify(t704)
    signals.append(t704)
    t705 = t472 & t29;

    t705 = mySimplify(t705)
    signals.append(t705)
    t706 = t704 ^ t705;

    t706 = mySimplify(t706)
    signals.append(t706)
    t707 = t370 & t37;

    t707 = mySimplify(t707)
    signals.append(t707)
    t708 = t707 ^ r0_138_18372;

    t708 = mySimplify(t708)
    signals.append(t708)
    t709 = t370 & t39;

    t709 = mySimplify(t709)
    signals.append(t709)
    t710 = t708 ^ t709;

    t710 = mySimplify(t710)
    signals.append(t710)
    t711 = t372 & t37;

    t711 = mySimplify(t711)
    signals.append(t711)
    t712 = t710 ^ t711;

    t712 = mySimplify(t712)
    signals.append(t712)
    t713 = t371 & t38;

    t713 = mySimplify(t713)
    signals.append(t713)
    t714 = t713 ^ r1_138_18373;

    t714 = mySimplify(t714)
    signals.append(t714)
    t715 = t370 & t38;

    t715 = mySimplify(t715)
    signals.append(t715)
    t716 = t714 ^ t715;

    t716 = mySimplify(t716)
    signals.append(t716)
    t717 = t371 & t37;

    t717 = mySimplify(t717)
    signals.append(t717)
    t718 = t716 ^ t717;

    t718 = mySimplify(t718)
    signals.append(t718)
    t719 = t372 & t39;

    t719 = mySimplify(t719)
    signals.append(t719)
    t720 = t719 ^ r0_138_18372;

    t720 = mySimplify(t720)
    signals.append(t720)
    t721 = t720 ^ r1_138_18373;

    t721 = mySimplify(t721)
    signals.append(t721)
    t722 = t371 & t39;

    t722 = mySimplify(t722)
    signals.append(t722)
    t723 = t721 ^ t722;

    t723 = mySimplify(t723)
    signals.append(t723)
    t724 = t372 & t38;

    t724 = mySimplify(t724)
    signals.append(t724)
    t725 = t723 ^ t724;

    t725 = mySimplify(t725)
    signals.append(t725)
    t726 = t473 & t19;

    t726 = mySimplify(t726)
    signals.append(t726)
    t727 = t726 ^ r0_139_18374;

    t727 = mySimplify(t727)
    signals.append(t727)
    t728 = t473 & t21;

    t728 = mySimplify(t728)
    signals.append(t728)
    t729 = t727 ^ t728;

    t729 = mySimplify(t729)
    signals.append(t729)
    t730 = t475 & t19;

    t730 = mySimplify(t730)
    signals.append(t730)
    t731 = t729 ^ t730;

    t731 = mySimplify(t731)
    signals.append(t731)
    t732 = t474 & t20;

    t732 = mySimplify(t732)
    signals.append(t732)
    t733 = t732 ^ r1_139_18375;

    t733 = mySimplify(t733)
    signals.append(t733)
    t734 = t473 & t20;

    t734 = mySimplify(t734)
    signals.append(t734)
    t735 = t733 ^ t734;

    t735 = mySimplify(t735)
    signals.append(t735)
    t736 = t474 & t19;

    t736 = mySimplify(t736)
    signals.append(t736)
    t737 = t735 ^ t736;

    t737 = mySimplify(t737)
    signals.append(t737)
    t738 = t475 & t21;

    t738 = mySimplify(t738)
    signals.append(t738)
    t739 = t738 ^ r0_139_18374;

    t739 = mySimplify(t739)
    signals.append(t739)
    t740 = t739 ^ r1_139_18375;

    t740 = mySimplify(t740)
    signals.append(t740)
    t741 = t474 & t21;

    t741 = mySimplify(t741)
    signals.append(t741)
    t742 = t740 ^ t741;

    t742 = mySimplify(t742)
    signals.append(t742)
    t743 = t475 & t20;

    t743 = mySimplify(t743)
    signals.append(t743)
    t744 = t742 ^ t743;

    t744 = mySimplify(t744)
    signals.append(t744)
    t745 = t370 & r_18014;

    t745 = mySimplify(t745)
    signals.append(t745)
    t746 = t745 ^ r0_140_18376;

    t746 = mySimplify(t746)
    signals.append(t746)
    t747 = t370 & t15;

    t747 = mySimplify(t747)
    signals.append(t747)
    t748 = t746 ^ t747;

    t748 = mySimplify(t748)
    signals.append(t748)
    t749 = t372 & r_18014;

    t749 = mySimplify(t749)
    signals.append(t749)
    t750 = t748 ^ t749;

    t750 = mySimplify(t750)
    signals.append(t750)
    t751 = t371 & r_18015;

    t751 = mySimplify(t751)
    signals.append(t751)
    t752 = t751 ^ r1_140_18377;

    t752 = mySimplify(t752)
    signals.append(t752)
    t753 = t370 & r_18015;

    t753 = mySimplify(t753)
    signals.append(t753)
    t754 = t752 ^ t753;

    t754 = mySimplify(t754)
    signals.append(t754)
    t755 = t371 & r_18014;

    t755 = mySimplify(t755)
    signals.append(t755)
    t756 = t754 ^ t755;

    t756 = mySimplify(t756)
    signals.append(t756)
    t757 = t372 & t15;

    t757 = mySimplify(t757)
    signals.append(t757)
    t758 = t757 ^ r0_140_18376;

    t758 = mySimplify(t758)
    signals.append(t758)
    t759 = t758 ^ r1_140_18377;

    t759 = mySimplify(t759)
    signals.append(t759)
    t760 = t371 & t15;

    t760 = mySimplify(t760)
    signals.append(t760)
    t761 = t759 ^ t760;

    t761 = mySimplify(t761)
    signals.append(t761)
    t762 = t372 & r_18015;

    t762 = mySimplify(t762)
    signals.append(t762)
    t763 = t761 ^ t762;

    t763 = mySimplify(t763)
    signals.append(t763)
    t764 = t473 & t76;

    t764 = mySimplify(t764)
    signals.append(t764)
    t765 = t764 ^ r0_141_18378;

    t765 = mySimplify(t765)
    signals.append(t765)
    t766 = t473 & t78;

    t766 = mySimplify(t766)
    signals.append(t766)
    t767 = t765 ^ t766;

    t767 = mySimplify(t767)
    signals.append(t767)
    t768 = t475 & t76;

    t768 = mySimplify(t768)
    signals.append(t768)
    t769 = t767 ^ t768;

    t769 = mySimplify(t769)
    signals.append(t769)
    t770 = t474 & t77;

    t770 = mySimplify(t770)
    signals.append(t770)
    t771 = t770 ^ r1_141_18379;

    t771 = mySimplify(t771)
    signals.append(t771)
    t772 = t473 & t77;

    t772 = mySimplify(t772)
    signals.append(t772)
    t773 = t771 ^ t772;

    t773 = mySimplify(t773)
    signals.append(t773)
    t774 = t474 & t76;

    t774 = mySimplify(t774)
    signals.append(t774)
    t775 = t773 ^ t774;

    t775 = mySimplify(t775)
    signals.append(t775)
    t776 = t475 & t78;

    t776 = mySimplify(t776)
    signals.append(t776)
    t777 = t776 ^ r0_141_18378;

    t777 = mySimplify(t777)
    signals.append(t777)
    t778 = t777 ^ r1_141_18379;

    t778 = mySimplify(t778)
    signals.append(t778)
    t779 = t474 & t78;

    t779 = mySimplify(t779)
    signals.append(t779)
    t780 = t778 ^ t779;

    t780 = mySimplify(t780)
    signals.append(t780)
    t781 = t475 & t77;

    t781 = mySimplify(t781)
    signals.append(t781)
    t782 = t780 ^ t781;

    t782 = mySimplify(t782)
    signals.append(t782)
    t783 = t617 ^ t674;

    t783 = mySimplify(t783)
    signals.append(t783)
    t784 = t623 ^ t680;

    t784 = mySimplify(t784)
    signals.append(t784)
    t785 = t630 ^ t687;

    t785 = mySimplify(t785)
    signals.append(t785)
    t786 = t541 ^ t712;

    t786 = mySimplify(t786)
    signals.append(t786)
    t787 = t547 ^ t718;

    t787 = mySimplify(t787)
    signals.append(t787)
    t788 = t554 ^ t725;

    t788 = mySimplify(t788)
    signals.append(t788)
    t789 = t450 ^ t598;

    t789 = mySimplify(t789)
    signals.append(t789)
    t790 = t456 ^ t604;

    t790 = mySimplify(t790)
    signals.append(t790)
    t791 = t463 ^ t611;

    t791 = mySimplify(t791)
    signals.append(t791)
    t792 = t522 ^ t541;

    t792 = mySimplify(t792)
    signals.append(t792)
    t793 = t528 ^ t547;

    t793 = mySimplify(t793)
    signals.append(t793)
    t794 = t535 ^ t554;

    t794 = mySimplify(t794)
    signals.append(t794)
    t795 = t750 ^ t731;

    t795 = mySimplify(t795)
    signals.append(t795)
    t796 = t756 ^ t737;

    t796 = mySimplify(t796)
    signals.append(t796)
    t797 = t763 ^ t744;

    t797 = mySimplify(t797)
    signals.append(t797)
    t798 = t750 ^ t450;

    t798 = mySimplify(t798)
    signals.append(t798)
    t799 = t756 ^ t456;

    t799 = mySimplify(t799)
    signals.append(t799)
    t800 = t763 ^ t463;

    t800 = mySimplify(t800)
    signals.append(t800)
    t801 = t636 ^ t655;

    t801 = mySimplify(t801)
    signals.append(t801)
    t802 = t642 ^ t661;

    t802 = mySimplify(t802)
    signals.append(t802)
    t803 = t649 ^ t668;

    t803 = mySimplify(t803)
    signals.append(t803)
    t804 = t484 ^ t769;

    t804 = mySimplify(t804)
    signals.append(t804)
    t805 = t490 ^ t775;

    t805 = mySimplify(t805)
    signals.append(t805)
    t806 = t497 ^ t782;

    t806 = mySimplify(t806)
    signals.append(t806)
    t807 = t579 ^ t636;

    t807 = mySimplify(t807)
    signals.append(t807)
    t808 = t585 ^ t642;

    t808 = mySimplify(t808)
    signals.append(t808)
    t809 = t592 ^ t649;

    t809 = mySimplify(t809)
    signals.append(t809)
    t810 = t674 ^ t693;

    t810 = mySimplify(t810)
    signals.append(t810)
    t811 = t680 ^ t699;

    t811 = mySimplify(t811)
    signals.append(t811)
    t812 = t687 ^ t706;

    t812 = mySimplify(t812)
    signals.append(t812)
    t813 = t731 ^ t789;

    t813 = mySimplify(t813)
    signals.append(t813)
    t814 = t737 ^ t790;

    t814 = mySimplify(t814)
    signals.append(t814)
    t815 = t744 ^ t791;

    t815 = mySimplify(t815)
    signals.append(t815)
    t816 = t795 ^ t804;

    t816 = mySimplify(t816)
    signals.append(t816)
    t817 = t796 ^ t805;

    t817 = mySimplify(t817)
    signals.append(t817)
    t818 = t797 ^ t806;

    t818 = mySimplify(t818)
    signals.append(t818)
    t819 = t560 ^ t783;

    t819 = mySimplify(t819)
    signals.append(t819)
    t820 = t566 ^ t784;

    t820 = mySimplify(t820)
    signals.append(t820)
    t821 = t573 ^ t785;

    t821 = mySimplify(t821)
    signals.append(t821)
    t822 = t769 ^ t807;

    t822 = mySimplify(t822)
    signals.append(t822)
    t823 = t775 ^ t808;

    t823 = mySimplify(t823)
    signals.append(t823)
    t824 = t782 ^ t809;

    t824 = mySimplify(t824)
    signals.append(t824)
    t825 = t783 ^ t816;

    t825 = mySimplify(t825)
    signals.append(t825)
    t826 = t784 ^ t817;

    t826 = mySimplify(t826)
    signals.append(t826)
    t827 = t785 ^ t818;

    t827 = mySimplify(t827)
    signals.append(t827)
    t828 = t387 ^ t816;

    t828 = mySimplify(t828)
    signals.append(t828)
    t829 = t393 ^ t817;

    t829 = mySimplify(t829)
    signals.append(t829)
    t830 = t400 ^ t818;

    t830 = mySimplify(t830)
    signals.append(t830)
    t831 = t801 ^ t819;

    t831 = mySimplify(t831)
    signals.append(t831)
    t832 = t802 ^ t820;

    t832 = mySimplify(t832)
    signals.append(t832)
    t833 = t803 ^ t821;

    t833 = mySimplify(t833)
    signals.append(t833)
    t834 = t792 ^ t819;

    t834 = mySimplify(t834)
    signals.append(t834)
    t835 = t793 ^ t820;

    t835 = mySimplify(t835)
    signals.append(t835)
    t836 = t794 ^ t821;

    t836 = mySimplify(t836)
    signals.append(t836)
    t837 = t560 ^ t822;

    t837 = mySimplify(t837)
    signals.append(t837)
    t838 = t566 ^ t823;

    t838 = mySimplify(t838)
    signals.append(t838)
    t839 = t573 ^ t824;

    t839 = mySimplify(t839)
    signals.append(t839)
    t840 = t828 ^ t831;

    t840 = mySimplify(t840)
    signals.append(t840)
    t841 = t829 ^ t832;

    t841 = mySimplify(t841)
    signals.append(t841)
    t842 = t830 ^ t833;

    t842 = mySimplify(t842)
    signals.append(t842)
    t843 = t503 ^ t834;

    t843 = mySimplify(t843)
    signals.append(t843)
    t844 = t509 ^ t835;

    t844 = mySimplify(t844)
    signals.append(t844)
    t845 = t516 ^ t836;

    t845 = mySimplify(t845)
    signals.append(t845)
    t846 = t822 ^ t834;

    t846 = mySimplify(t846)
    signals.append(t846)
    t847 = t823 ^ t835;

    t847 = mySimplify(t847)
    signals.append(t847)
    t848 = t824 ^ t836;

    t848 = mySimplify(t848)
    signals.append(t848)
    t849 = t813 ^ t831;

    t849 = mySimplify(t849)
    signals.append(t849)
    t850 = t814 ^ t832;

    t850 = mySimplify(t850)
    signals.append(t850)
    t851 = t815 ^ t833;

    t851 = mySimplify(t851)
    signals.append(t851)
    t852 = t789 ^ t825;

    t852 = mySimplify(t852)
    signals.append(t852)
    t853 = t790 ^ t826;

    t853 = mySimplify(t853)
    signals.append(t853)
    t854 = t791 ^ t827;

    t854 = mySimplify(t854)
    signals.append(t854)
    t855 = t837 ^ t840;

    t855 = mySimplify(t855)
    signals.append(t855)
    t856 = t838 ^ t841;

    t856 = mySimplify(t856)
    signals.append(t856)
    t857 = t839 ^ t842;

    t857 = mySimplify(t857)
    signals.append(t857)
    t858 = t804 ^ t843;

    t858 = mySimplify(t858)
    signals.append(t858)
    t859 = t805 ^ t844;

    t859 = mySimplify(t859)
    signals.append(t859)
    t860 = t806 ^ t845;

    t860 = mySimplify(t860)
    signals.append(t860)
    t861 = t798 ^ t843;

    t861 = mySimplify(t861)
    signals.append(t861)
    t862 = t799 ^ t844;

    t862 = mySimplify(t862)
    signals.append(t862)
    t863 = t800 ^ t845;

    t863 = mySimplify(t863)
    signals.append(t863)
    t864 = t786 ^ t840;

    t864 = mySimplify(t864)
    signals.append(t864)
    t865 = t787 ^ t841;

    t865 = mySimplify(t865)
    signals.append(t865)
    t866 = t788 ^ t842;

    t866 = mySimplify(t866)
    signals.append(t866)
    t867 = t837 ^ t858;

    t867 = mySimplify(t867)
    signals.append(t867)
    t868 = t838 ^ t859;

    t868 = mySimplify(t868)
    signals.append(t868)
    t869 = t839 ^ t860;

    t869 = mySimplify(t869)
    signals.append(t869)
    t870 = t810 ^ t855;

    t870 = mySimplify(t870)
    signals.append(t870)
    t871 = t811 ^ t856;

    t871 = mySimplify(t871)
    signals.append(t871)
    t872 = t812 ^ t857;

    t872 = mySimplify(t872)
    signals.append(t872)


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

                c1, c2 = uma1(m0, m1, z12, r0, r1, k0, k1)
 
                r_ref = k0 & k1
                r_ref = mySimplify(r_ref)
                r = c1 ^ c2
                r = mySimplify(r)

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


