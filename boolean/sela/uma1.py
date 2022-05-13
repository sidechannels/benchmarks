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



    r_1640 = symbol('r_1640', 'M', 1)
    r_1641 = symbol('r_1641', 'M', 1)
    r_1642 = symbol('r_1642', 'M', 1)
    r_1643 = symbol('r_1643', 'M', 1)
    r_1644 = symbol('r_1644', 'M', 1)
    r_1645 = symbol('r_1645', 'M', 1)
    r_1646 = symbol('r_1646', 'M', 1)
    r_1647 = symbol('r_1647', 'M', 1)
    r0_64_1678 = symbol('r0_64_1678', 'M', 1)
    r0_65_1679 = symbol('r0_65_1679', 'M', 1)
    r0_66_16710 = symbol('r0_66_16710', 'M', 1)
    r0_67_16711 = symbol('r0_67_16711', 'M', 1)
    r0_68_16712 = symbol('r0_68_16712', 'M', 1)
    r0_69_16713 = symbol('r0_69_16713', 'M', 1)
    r0_70_16714 = symbol('r0_70_16714', 'M', 1)
    r0_71_16715 = symbol('r0_71_16715', 'M', 1)
    r0_81_16716 = symbol('r0_81_16716', 'M', 1)
    r0_82_16717 = symbol('r0_82_16717', 'M', 1)
    r0_92_16718 = symbol('r0_92_16718', 'M', 1)
    r0_93_16719 = symbol('r0_93_16719', 'M', 1)
    r0_99_16720 = symbol('r0_99_16720', 'M', 1)
    r0_100_16721 = symbol('r0_100_16721', 'M', 1)
    r0_103_16722 = symbol('r0_103_16722', 'M', 1)
    r0_104_16723 = symbol('r0_104_16723', 'M', 1)
    r0_110_16724 = symbol('r0_110_16724', 'M', 1)
    r0_111_16725 = symbol('r0_111_16725', 'M', 1)
    r0_112_16726 = symbol('r0_112_16726', 'M', 1)
    r0_113_16727 = symbol('r0_113_16727', 'M', 1)
    r0_114_16728 = symbol('r0_114_16728', 'M', 1)
    r0_115_16729 = symbol('r0_115_16729', 'M', 1)
    r0_116_16730 = symbol('r0_116_16730', 'M', 1)
    r0_117_16731 = symbol('r0_117_16731', 'M', 1)
    r0_118_16732 = symbol('r0_118_16732', 'M', 1)
    r0_119_16733 = symbol('r0_119_16733', 'M', 1)
    r0_120_16734 = symbol('r0_120_16734', 'M', 1)
    r0_121_16735 = symbol('r0_121_16735', 'M', 1)
    r0_122_16736 = symbol('r0_122_16736', 'M', 1)
    r0_123_16737 = symbol('r0_123_16737', 'M', 1)
    r0_124_16738 = symbol('r0_124_16738', 'M', 1)
    r0_125_16739 = symbol('r0_125_16739', 'M', 1)


    signals = []
    t0 = k0 ^ r_1640;
    t0 = mySimplify(t0)
    signals.append(t0)
    t1 = k1 ^ r_1641;

    t1 = mySimplify(t1)
    signals.append(t1)
    t2 = k2 ^ r_1642;

    t2 = mySimplify(t2)
    signals.append(t2)
    t3 = k3 ^ r_1643;

    t3 = mySimplify(t3)
    signals.append(t3)
    t4 = k4 ^ r_1644;

    t4 = mySimplify(t4)
    signals.append(t4)
    t5 = k5 ^ r_1645;

    t5 = mySimplify(t5)
    signals.append(t5)
    t6 = k6 ^ r_1646;

    t6 = mySimplify(t6)
    signals.append(t6)
    t7 = k7 ^ r_1647;

    t7 = mySimplify(t7)
    signals.append(t7)
    t8 = r_1643 ^ r_1645;

    t8 = mySimplify(t8)
    signals.append(t8)
    t9 = t3 ^ t5;

    t9 = mySimplify(t9)
    signals.append(t9)
    t10 = r_1640 ^ r_1646;

    t10 = mySimplify(t10)
    signals.append(t10)
    t11 = t0 ^ t6;

    t11 = mySimplify(t11)
    signals.append(t11)
    t12 = t10 ^ t8;

    t12 = mySimplify(t12)
    signals.append(t12)
    t13 = t11 ^ t9;

    t13 = mySimplify(t13)
    signals.append(t13)
    t14 = r_1640 ^ r_1643;

    t14 = mySimplify(t14)
    signals.append(t14)
    t15 = t0 ^ t3;

    t15 = mySimplify(t15)
    signals.append(t15)
    t16 = r_1640 ^ r_1645;

    t16 = mySimplify(t16)
    signals.append(t16)
    t17 = t0 ^ t5;

    t17 = mySimplify(t17)
    signals.append(t17)
    t18 = r_1641 ^ r_1642;

    t18 = mySimplify(t18)
    signals.append(t18)
    t19 = t1 ^ t2;

    t19 = mySimplify(t19)
    signals.append(t19)
    t20 = t18 ^ r_1647;

    t20 = mySimplify(t20)
    signals.append(t20)
    t21 = t19 ^ t7;

    t21 = mySimplify(t21)
    signals.append(t21)
    t22 = t20 ^ r_1643;

    t22 = mySimplify(t22)
    signals.append(t22)
    t23 = t21 ^ t3;

    t23 = mySimplify(t23)
    signals.append(t23)
    t24 = t20 ^ r_1640;

    t24 = mySimplify(t24)
    signals.append(t24)
    t25 = t21 ^ t0;

    t25 = mySimplify(t25)
    signals.append(t25)
    t26 = t20 ^ r_1646;

    t26 = mySimplify(t26)
    signals.append(t26)
    t27 = t21 ^ t6;

    t27 = mySimplify(t27)
    signals.append(t27)
    t28 = r_1644 ^ t12;

    t28 = mySimplify(t28)
    signals.append(t28)
    t29 = t4 ^ t13;

    t29 = mySimplify(t29)
    signals.append(t29)
    t30 = t26 ^ t16;

    t30 = mySimplify(t30)
    signals.append(t30)
    t31 = t27 ^ t17;

    t31 = mySimplify(t31)
    signals.append(t31)
    t32 = t28 ^ r_1645;

    t32 = mySimplify(t32)
    signals.append(t32)
    t33 = t29 ^ t5;

    t33 = mySimplify(t33)
    signals.append(t33)
    t34 = t28 ^ r_1641;

    t34 = mySimplify(t34)
    signals.append(t34)
    t35 = t29 ^ t1;

    t35 = mySimplify(t35)
    signals.append(t35)
    t36 = t32 ^ r_1647;

    t36 = mySimplify(t36)
    signals.append(t36)
    t37 = t33 ^ t7;

    t37 = mySimplify(t37)
    signals.append(t37)
    t38 = t32 ^ t18;

    t38 = mySimplify(t38)
    signals.append(t38)
    t39 = t33 ^ t19;

    t39 = mySimplify(t39)
    signals.append(t39)
    t40 = t34 ^ t14;

    t40 = mySimplify(t40)
    signals.append(t40)
    t41 = t35 ^ t15;

    t41 = mySimplify(t41)
    signals.append(t41)
    t42 = r_1647 ^ t40;

    t42 = mySimplify(t42)
    signals.append(t42)
    t43 = t7 ^ t41;

    t43 = mySimplify(t43)
    signals.append(t43)
    t44 = t38 ^ t40;

    t44 = mySimplify(t44)
    signals.append(t44)
    t45 = t39 ^ t41;

    t45 = mySimplify(t45)
    signals.append(t45)
    t46 = t38 ^ t16;

    t46 = mySimplify(t46)
    signals.append(t46)
    t47 = t39 ^ t17;

    t47 = mySimplify(t47)
    signals.append(t47)
    t48 = t18 ^ t40;

    t48 = mySimplify(t48)
    signals.append(t48)
    t49 = t19 ^ t41;

    t49 = mySimplify(t49)
    signals.append(t49)
    t50 = t10 ^ t48;

    t50 = mySimplify(t50)
    signals.append(t50)
    t51 = t11 ^ t49;

    t51 = mySimplify(t51)
    signals.append(t51)
    t52 = r_1640 ^ t48;

    t52 = mySimplify(t52)
    signals.append(t52)
    t53 = t0 ^ t49;

    t53 = mySimplify(t53)
    signals.append(t53)
    t54 = t12 & t32;

    t54 = mySimplify(t54)
    signals.append(t54)
    t55 = t13 & t33;

    t55 = mySimplify(t55)
    signals.append(t55)
    t56 = t12 & t33;

    t56 = mySimplify(t56)
    signals.append(t56)
    t57 = t13 & t32;

    t57 = mySimplify(t57)
    signals.append(t57)
    t58 = t54 ^ r0_64_1678;

    t58 = mySimplify(t58)
    signals.append(t58)
    t59 = t58 ^ t56;

    t59 = mySimplify(t59)
    signals.append(t59)
    t60 = t55 ^ r0_64_1678;

    t60 = mySimplify(t60)
    signals.append(t60)
    t61 = t60 ^ t57;

    t61 = mySimplify(t61)
    signals.append(t61)
    t62 = t30 & t36;

    t62 = mySimplify(t62)
    signals.append(t62)
    t63 = t31 & t37;

    t63 = mySimplify(t63)
    signals.append(t63)
    t64 = t30 & t37;

    t64 = mySimplify(t64)
    signals.append(t64)
    t65 = t31 & t36;

    t65 = mySimplify(t65)
    signals.append(t65)
    t66 = t62 ^ r0_65_1679;

    t66 = mySimplify(t66)
    signals.append(t66)
    t67 = t66 ^ t64;

    t67 = mySimplify(t67)
    signals.append(t67)
    t68 = t63 ^ r0_65_1679;

    t68 = mySimplify(t68)
    signals.append(t68)
    t69 = t68 ^ t65;

    t69 = mySimplify(t69)
    signals.append(t69)
    t70 = t22 & r_1647;

    t70 = mySimplify(t70)
    signals.append(t70)
    t71 = t23 & t7;

    t71 = mySimplify(t71)
    signals.append(t71)
    t72 = t22 & t7;

    t72 = mySimplify(t72)
    signals.append(t72)
    t73 = t23 & r_1647;

    t73 = mySimplify(t73)
    signals.append(t73)
    t74 = t70 ^ r0_66_16710;

    t74 = mySimplify(t74)
    signals.append(t74)
    t75 = t74 ^ t72;

    t75 = mySimplify(t75)
    signals.append(t75)
    t76 = t71 ^ r0_66_16710;

    t76 = mySimplify(t76)
    signals.append(t76)
    t77 = t76 ^ t73;

    t77 = mySimplify(t77)
    signals.append(t77)
    t78 = t10 & t48;

    t78 = mySimplify(t78)
    signals.append(t78)
    t79 = t11 & t49;

    t79 = mySimplify(t79)
    signals.append(t79)
    t80 = t10 & t49;

    t80 = mySimplify(t80)
    signals.append(t80)
    t81 = t11 & t48;

    t81 = mySimplify(t81)
    signals.append(t81)
    t82 = t78 ^ r0_67_16711;

    t82 = mySimplify(t82)
    signals.append(t82)
    t83 = t82 ^ t80;

    t83 = mySimplify(t83)
    signals.append(t83)
    t84 = t79 ^ r0_67_16711;

    t84 = mySimplify(t84)
    signals.append(t84)
    t85 = t84 ^ t81;

    t85 = mySimplify(t85)
    signals.append(t85)
    t86 = t26 & t20;

    t86 = mySimplify(t86)
    signals.append(t86)
    t87 = t27 & t21;

    t87 = mySimplify(t87)
    signals.append(t87)
    t88 = t26 & t21;

    t88 = mySimplify(t88)
    signals.append(t88)
    t89 = t27 & t20;

    t89 = mySimplify(t89)
    signals.append(t89)
    t90 = t86 ^ r0_68_16712;

    t90 = mySimplify(t90)
    signals.append(t90)
    t91 = t90 ^ t88;

    t91 = mySimplify(t91)
    signals.append(t91)
    t92 = t87 ^ r0_68_16712;

    t92 = mySimplify(t92)
    signals.append(t92)
    t93 = t92 ^ t89;

    t93 = mySimplify(t93)
    signals.append(t93)
    t94 = t24 & t42;

    t94 = mySimplify(t94)
    signals.append(t94)
    t95 = t25 & t43;

    t95 = mySimplify(t95)
    signals.append(t95)
    t96 = t24 & t43;

    t96 = mySimplify(t96)
    signals.append(t96)
    t97 = t25 & t42;

    t97 = mySimplify(t97)
    signals.append(t97)
    t98 = t94 ^ r0_69_16713;

    t98 = mySimplify(t98)
    signals.append(t98)
    t99 = t98 ^ t96;

    t99 = mySimplify(t99)
    signals.append(t99)
    t100 = t95 ^ r0_69_16713;

    t100 = mySimplify(t100)
    signals.append(t100)
    t101 = t100 ^ t97;

    t101 = mySimplify(t101)
    signals.append(t101)
    t102 = t14 & t40;

    t102 = mySimplify(t102)
    signals.append(t102)
    t103 = t15 & t41;

    t103 = mySimplify(t103)
    signals.append(t103)
    t104 = t14 & t41;

    t104 = mySimplify(t104)
    signals.append(t104)
    t105 = t15 & t40;

    t105 = mySimplify(t105)
    signals.append(t105)
    t106 = t102 ^ r0_70_16714;

    t106 = mySimplify(t106)
    signals.append(t106)
    t107 = t106 ^ t104;

    t107 = mySimplify(t107)
    signals.append(t107)
    t108 = t103 ^ r0_70_16714;

    t108 = mySimplify(t108)
    signals.append(t108)
    t109 = t108 ^ t105;

    t109 = mySimplify(t109)
    signals.append(t109)
    t110 = t8 & t44;

    t110 = mySimplify(t110)
    signals.append(t110)
    t111 = t9 & t45;

    t111 = mySimplify(t111)
    signals.append(t111)
    t112 = t8 & t45;

    t112 = mySimplify(t112)
    signals.append(t112)
    t113 = t9 & t44;

    t113 = mySimplify(t113)
    signals.append(t113)
    t114 = t110 ^ r0_71_16715;

    t114 = mySimplify(t114)
    signals.append(t114)
    t115 = t114 ^ t112;

    t115 = mySimplify(t115)
    signals.append(t115)
    t116 = t111 ^ r0_71_16715;

    t116 = mySimplify(t116)
    signals.append(t116)
    t117 = t116 ^ t113;

    t117 = mySimplify(t117)
    signals.append(t117)
    t118 = t67 ^ t59;

    t118 = mySimplify(t118)
    signals.append(t118)
    t119 = t69 ^ t61;

    t119 = mySimplify(t119)
    signals.append(t119)
    t120 = t75 ^ t59;

    t120 = mySimplify(t120)
    signals.append(t120)
    t121 = t77 ^ t61;

    t121 = mySimplify(t121)
    signals.append(t121)
    t122 = t91 ^ t83;

    t122 = mySimplify(t122)
    signals.append(t122)
    t123 = t93 ^ t85;

    t123 = mySimplify(t123)
    signals.append(t123)
    t124 = t99 ^ t83;

    t124 = mySimplify(t124)
    signals.append(t124)
    t125 = t101 ^ t85;

    t125 = mySimplify(t125)
    signals.append(t125)
    t126 = t115 ^ t107;

    t126 = mySimplify(t126)
    signals.append(t126)
    t127 = t117 ^ t109;

    t127 = mySimplify(t127)
    signals.append(t127)
    t128 = t118 ^ t126;

    t128 = mySimplify(t128)
    signals.append(t128)
    t129 = t119 ^ t127;

    t129 = mySimplify(t129)
    signals.append(t129)
    t130 = t122 ^ t126;

    t130 = mySimplify(t130)
    signals.append(t130)
    t131 = t123 ^ t127;

    t131 = mySimplify(t131)
    signals.append(t131)
    t132 = t128 ^ t34;

    t132 = mySimplify(t132)
    signals.append(t132)
    t133 = t129 ^ t35;

    t133 = mySimplify(t133)
    signals.append(t133)
    t134 = t130 ^ t50;

    t134 = mySimplify(t134)
    signals.append(t134)
    t135 = t131 ^ t51;

    t135 = mySimplify(t135)
    signals.append(t135)
    t136 = t16 & t38;

    t136 = mySimplify(t136)
    signals.append(t136)
    t137 = t17 & t39;

    t137 = mySimplify(t137)
    signals.append(t137)
    t138 = t16 & t39;

    t138 = mySimplify(t138)
    signals.append(t138)
    t139 = t17 & t38;

    t139 = mySimplify(t139)
    signals.append(t139)
    t140 = t136 ^ r0_81_16716;

    t140 = mySimplify(t140)
    signals.append(t140)
    t141 = t140 ^ t138;

    t141 = mySimplify(t141)
    signals.append(t141)
    t142 = t137 ^ r0_81_16716;

    t142 = mySimplify(t142)
    signals.append(t142)
    t143 = t142 ^ t139;

    t143 = mySimplify(t143)
    signals.append(t143)
    t144 = t132 & t134;

    t144 = mySimplify(t144)
    signals.append(t144)
    t145 = t133 & t135;

    t145 = mySimplify(t145)
    signals.append(t145)
    t146 = t132 & t135;

    t146 = mySimplify(t146)
    signals.append(t146)
    t147 = t133 & t134;

    t147 = mySimplify(t147)
    signals.append(t147)
    t148 = t144 ^ r0_82_16717;

    t148 = mySimplify(t148)
    signals.append(t148)
    t149 = t148 ^ t146;

    t149 = mySimplify(t149)
    signals.append(t149)
    t150 = t145 ^ r0_82_16717;

    t150 = mySimplify(t150)
    signals.append(t150)
    t151 = t150 ^ t147;

    t151 = mySimplify(t151)
    signals.append(t151)
    t152 = t141 ^ t107;

    t152 = mySimplify(t152)
    signals.append(t152)
    t153 = t143 ^ t109;

    t153 = mySimplify(t153)
    signals.append(t153)
    t154 = t120 ^ t152;

    t154 = mySimplify(t154)
    signals.append(t154)
    t155 = t121 ^ t153;

    t155 = mySimplify(t155)
    signals.append(t155)
    t156 = t124 ^ t152;

    t156 = mySimplify(t156)
    signals.append(t156)
    t157 = t125 ^ t153;

    t157 = mySimplify(t157)
    signals.append(t157)
    t158 = t156 ^ t52;

    t158 = mySimplify(t158)
    signals.append(t158)
    t159 = t157 ^ t53;

    t159 = mySimplify(t159)
    signals.append(t159)
    t160 = t134 ^ t158;

    t160 = mySimplify(t160)
    signals.append(t160)
    t161 = t135 ^ t159;

    t161 = mySimplify(t161)
    signals.append(t161)
    t162 = t154 ^ t46;

    t162 = mySimplify(t162)
    signals.append(t162)
    t163 = t155 ^ t47;

    t163 = mySimplify(t163)
    signals.append(t163)
    t164 = t132 ^ t162;

    t164 = mySimplify(t164)
    signals.append(t164)
    t165 = t133 ^ t163;

    t165 = mySimplify(t165)
    signals.append(t165)
    t166 = t158 ^ t149;

    t166 = mySimplify(t166)
    signals.append(t166)
    t167 = t159 ^ t151;

    t167 = mySimplify(t167)
    signals.append(t167)
    t168 = t162 ^ t149;

    t168 = mySimplify(t168)
    signals.append(t168)
    t169 = t163 ^ t151;

    t169 = mySimplify(t169)
    signals.append(t169)
    t170 = t164 & t166;

    t170 = mySimplify(t170)
    signals.append(t170)
    t171 = t165 & t167;

    t171 = mySimplify(t171)
    signals.append(t171)
    t172 = t164 & t167;

    t172 = mySimplify(t172)
    signals.append(t172)
    t173 = t165 & t166;

    t173 = mySimplify(t173)
    signals.append(t173)
    t174 = t170 ^ r0_92_16718;

    t174 = mySimplify(t174)
    signals.append(t174)
    t175 = t174 ^ t172;

    t175 = mySimplify(t175)
    signals.append(t175)
    t176 = t171 ^ r0_92_16718;

    t176 = mySimplify(t176)
    signals.append(t176)
    t177 = t176 ^ t173;

    t177 = mySimplify(t177)
    signals.append(t177)
    t178 = t168 & t160;

    t178 = mySimplify(t178)
    signals.append(t178)
    t179 = t169 & t161;

    t179 = mySimplify(t179)
    signals.append(t179)
    t180 = t168 & t161;

    t180 = mySimplify(t180)
    signals.append(t180)
    t181 = t169 & t160;

    t181 = mySimplify(t181)
    signals.append(t181)
    t182 = t178 ^ r0_93_16719;

    t182 = mySimplify(t182)
    signals.append(t182)
    t183 = t182 ^ t180;

    t183 = mySimplify(t183)
    signals.append(t183)
    t184 = t179 ^ r0_93_16719;

    t184 = mySimplify(t184)
    signals.append(t184)
    t185 = t184 ^ t181;

    t185 = mySimplify(t185)
    signals.append(t185)
    t186 = t175 ^ t162;

    t186 = mySimplify(t186)
    signals.append(t186)
    t187 = t177 ^ t163;

    t187 = mySimplify(t187)
    signals.append(t187)
    t188 = t183 ^ t158;

    t188 = mySimplify(t188)
    signals.append(t188)
    t189 = t185 ^ t159;

    t189 = mySimplify(t189)
    signals.append(t189)
    t190 = t134 ^ t188;

    t190 = mySimplify(t190)
    signals.append(t190)
    t191 = t135 ^ t189;

    t191 = mySimplify(t191)
    signals.append(t191)
    t192 = t166 ^ t188;

    t192 = mySimplify(t192)
    signals.append(t192)
    t193 = t167 ^ t189;

    t193 = mySimplify(t193)
    signals.append(t193)
    t194 = t186 ^ t188;

    t194 = mySimplify(t194)
    signals.append(t194)
    t195 = t187 ^ t189;

    t195 = mySimplify(t195)
    signals.append(t195)
    t196 = t186 & t24;

    t196 = mySimplify(t196)
    signals.append(t196)
    t197 = t187 & t25;

    t197 = mySimplify(t197)
    signals.append(t197)
    t198 = t186 & t25;

    t198 = mySimplify(t198)
    signals.append(t198)
    t199 = t187 & t24;

    t199 = mySimplify(t199)
    signals.append(t199)
    t200 = t196 ^ r0_99_16720;

    t200 = mySimplify(t200)
    signals.append(t200)
    t201 = t200 ^ t198;

    t201 = mySimplify(t201)
    signals.append(t201)
    t202 = t197 ^ r0_99_16720;

    t202 = mySimplify(t202)
    signals.append(t202)
    t203 = t202 ^ t199;

    t203 = mySimplify(t203)
    signals.append(t203)
    t204 = t158 & t192;

    t204 = mySimplify(t204)
    signals.append(t204)
    t205 = t159 & t193;

    t205 = mySimplify(t205)
    signals.append(t205)
    t206 = t158 & t193;

    t206 = mySimplify(t206)
    signals.append(t206)
    t207 = t159 & t192;

    t207 = mySimplify(t207)
    signals.append(t207)
    t208 = t204 ^ r0_100_16721;

    t208 = mySimplify(t208)
    signals.append(t208)
    t209 = t208 ^ t206;

    t209 = mySimplify(t209)
    signals.append(t209)
    t210 = t205 ^ r0_100_16721;

    t210 = mySimplify(t210)
    signals.append(t210)
    t211 = t210 ^ t207;

    t211 = mySimplify(t211)
    signals.append(t211)
    t212 = t209 ^ t190;

    t212 = mySimplify(t212)
    signals.append(t212)
    t213 = t211 ^ t191;

    t213 = mySimplify(t213)
    signals.append(t213)
    t214 = t166 ^ t209;

    t214 = mySimplify(t214)
    signals.append(t214)
    t215 = t167 ^ t211;

    t215 = mySimplify(t215)
    signals.append(t215)
    t216 = t186 & t214;

    t216 = mySimplify(t216)
    signals.append(t216)
    t217 = t187 & t215;

    t217 = mySimplify(t217)
    signals.append(t217)
    t218 = t186 & t215;

    t218 = mySimplify(t218)
    signals.append(t218)
    t219 = t187 & t214;

    t219 = mySimplify(t219)
    signals.append(t219)
    t220 = t216 ^ r0_103_16722;

    t220 = mySimplify(t220)
    signals.append(t220)
    t221 = t220 ^ t218;

    t221 = mySimplify(t221)
    signals.append(t221)
    t222 = t217 ^ r0_103_16722;

    t222 = mySimplify(t222)
    signals.append(t222)
    t223 = t222 ^ t219;

    t223 = mySimplify(t223)
    signals.append(t223)
    t224 = t186 & t42;

    t224 = mySimplify(t224)
    signals.append(t224)
    t225 = t187 & t43;

    t225 = mySimplify(t225)
    signals.append(t225)
    t226 = t186 & t43;

    t226 = mySimplify(t226)
    signals.append(t226)
    t227 = t187 & t42;

    t227 = mySimplify(t227)
    signals.append(t227)
    t228 = t224 ^ r0_104_16723;

    t228 = mySimplify(t228)
    signals.append(t228)
    t229 = t228 ^ t226;

    t229 = mySimplify(t229)
    signals.append(t229)
    t230 = t225 ^ r0_104_16723;

    t230 = mySimplify(t230)
    signals.append(t230)
    t231 = t230 ^ t227;

    t231 = mySimplify(t231)
    signals.append(t231)
    t232 = t188 ^ t212;

    t232 = mySimplify(t232)
    signals.append(t232)
    t233 = t189 ^ t213;

    t233 = mySimplify(t233)
    signals.append(t233)
    t234 = t164 ^ t221;

    t234 = mySimplify(t234)
    signals.append(t234)
    t235 = t165 ^ t223;

    t235 = mySimplify(t235)
    signals.append(t235)
    t236 = t234 ^ t212;

    t236 = mySimplify(t236)
    signals.append(t236)
    t237 = t235 ^ t213;

    t237 = mySimplify(t237)
    signals.append(t237)
    t238 = t186 ^ t234;

    t238 = mySimplify(t238)
    signals.append(t238)
    t239 = t187 ^ t235;

    t239 = mySimplify(t239)
    signals.append(t239)
    t240 = t194 ^ t236;

    t240 = mySimplify(t240)
    signals.append(t240)
    t241 = t195 ^ t237;

    t241 = mySimplify(t241)
    signals.append(t241)
    t242 = t232 & t32;

    t242 = mySimplify(t242)
    signals.append(t242)
    t243 = t233 & t33;

    t243 = mySimplify(t243)
    signals.append(t243)
    t244 = t232 & t33;

    t244 = mySimplify(t244)
    signals.append(t244)
    t245 = t233 & t32;

    t245 = mySimplify(t245)
    signals.append(t245)
    t246 = t242 ^ r0_110_16724;

    t246 = mySimplify(t246)
    signals.append(t246)
    t247 = t246 ^ t244;

    t247 = mySimplify(t247)
    signals.append(t247)
    t248 = t243 ^ r0_110_16724;

    t248 = mySimplify(t248)
    signals.append(t248)
    t249 = t248 ^ t245;

    t249 = mySimplify(t249)
    signals.append(t249)
    t250 = t212 & t36;

    t250 = mySimplify(t250)
    signals.append(t250)
    t251 = t213 & t37;

    t251 = mySimplify(t251)
    signals.append(t251)
    t252 = t212 & t37;

    t252 = mySimplify(t252)
    signals.append(t252)
    t253 = t213 & t36;

    t253 = mySimplify(t253)
    signals.append(t253)
    t254 = t250 ^ r0_111_16725;

    t254 = mySimplify(t254)
    signals.append(t254)
    t255 = t254 ^ t252;

    t255 = mySimplify(t255)
    signals.append(t255)
    t256 = t251 ^ r0_111_16725;

    t256 = mySimplify(t256)
    signals.append(t256)
    t257 = t256 ^ t253;

    t257 = mySimplify(t257)
    signals.append(t257)
    t258 = t232 & t12;

    t258 = mySimplify(t258)
    signals.append(t258)
    t259 = t233 & t13;

    t259 = mySimplify(t259)
    signals.append(t259)
    t260 = t232 & t13;

    t260 = mySimplify(t260)
    signals.append(t260)
    t261 = t233 & t12;

    t261 = mySimplify(t261)
    signals.append(t261)
    t262 = t258 ^ r0_112_16726;

    t262 = mySimplify(t262)
    signals.append(t262)
    t263 = t262 ^ t260;

    t263 = mySimplify(t263)
    signals.append(t263)
    t264 = t259 ^ r0_112_16726;

    t264 = mySimplify(t264)
    signals.append(t264)
    t265 = t264 ^ t261;

    t265 = mySimplify(t265)
    signals.append(t265)
    t266 = t212 & t30;

    t266 = mySimplify(t266)
    signals.append(t266)
    t267 = t213 & t31;

    t267 = mySimplify(t267)
    signals.append(t267)
    t268 = t212 & t31;

    t268 = mySimplify(t268)
    signals.append(t268)
    t269 = t213 & t30;

    t269 = mySimplify(t269)
    signals.append(t269)
    t270 = t266 ^ r0_113_16727;

    t270 = mySimplify(t270)
    signals.append(t270)
    t271 = t270 ^ t268;

    t271 = mySimplify(t271)
    signals.append(t271)
    t272 = t267 ^ r0_113_16727;

    t272 = mySimplify(t272)
    signals.append(t272)
    t273 = t272 ^ t269;

    t273 = mySimplify(t273)
    signals.append(t273)
    t274 = t234 & t20;

    t274 = mySimplify(t274)
    signals.append(t274)
    t275 = t235 & t21;

    t275 = mySimplify(t275)
    signals.append(t275)
    t276 = t234 & t21;

    t276 = mySimplify(t276)
    signals.append(t276)
    t277 = t235 & t20;

    t277 = mySimplify(t277)
    signals.append(t277)
    t278 = t274 ^ r0_114_16728;

    t278 = mySimplify(t278)
    signals.append(t278)
    t279 = t278 ^ t276;

    t279 = mySimplify(t279)
    signals.append(t279)
    t280 = t275 ^ r0_114_16728;

    t280 = mySimplify(t280)
    signals.append(t280)
    t281 = t280 ^ t277;

    t281 = mySimplify(t281)
    signals.append(t281)
    t282 = t194 & t40;

    t282 = mySimplify(t282)
    signals.append(t282)
    t283 = t195 & t41;

    t283 = mySimplify(t283)
    signals.append(t283)
    t284 = t194 & t41;

    t284 = mySimplify(t284)
    signals.append(t284)
    t285 = t195 & t40;

    t285 = mySimplify(t285)
    signals.append(t285)
    t286 = t282 ^ r0_115_16729;

    t286 = mySimplify(t286)
    signals.append(t286)
    t287 = t286 ^ t284;

    t287 = mySimplify(t287)
    signals.append(t287)
    t288 = t283 ^ r0_115_16729;

    t288 = mySimplify(t288)
    signals.append(t288)
    t289 = t288 ^ t285;

    t289 = mySimplify(t289)
    signals.append(t289)
    t290 = t234 & t26;

    t290 = mySimplify(t290)
    signals.append(t290)
    t291 = t235 & t27;

    t291 = mySimplify(t291)
    signals.append(t291)
    t292 = t234 & t27;

    t292 = mySimplify(t292)
    signals.append(t292)
    t293 = t235 & t26;

    t293 = mySimplify(t293)
    signals.append(t293)
    t294 = t290 ^ r0_116_16730;

    t294 = mySimplify(t294)
    signals.append(t294)
    t295 = t294 ^ t292;

    t295 = mySimplify(t295)
    signals.append(t295)
    t296 = t291 ^ r0_116_16730;

    t296 = mySimplify(t296)
    signals.append(t296)
    t297 = t296 ^ t293;

    t297 = mySimplify(t297)
    signals.append(t297)
    t298 = t194 & t14;

    t298 = mySimplify(t298)
    signals.append(t298)
    t299 = t195 & t15;

    t299 = mySimplify(t299)
    signals.append(t299)
    t300 = t194 & t15;

    t300 = mySimplify(t300)
    signals.append(t300)
    t301 = t195 & t14;

    t301 = mySimplify(t301)
    signals.append(t301)
    t302 = t298 ^ r0_117_16731;

    t302 = mySimplify(t302)
    signals.append(t302)
    t303 = t302 ^ t300;

    t303 = mySimplify(t303)
    signals.append(t303)
    t304 = t299 ^ r0_117_16731;

    t304 = mySimplify(t304)
    signals.append(t304)
    t305 = t304 ^ t301;

    t305 = mySimplify(t305)
    signals.append(t305)
    t306 = t240 & t44;

    t306 = mySimplify(t306)
    signals.append(t306)
    t307 = t241 & t45;

    t307 = mySimplify(t307)
    signals.append(t307)
    t308 = t240 & t45;

    t308 = mySimplify(t308)
    signals.append(t308)
    t309 = t241 & t44;

    t309 = mySimplify(t309)
    signals.append(t309)
    t310 = t306 ^ r0_118_16732;

    t310 = mySimplify(t310)
    signals.append(t310)
    t311 = t310 ^ t308;

    t311 = mySimplify(t311)
    signals.append(t311)
    t312 = t307 ^ r0_118_16732;

    t312 = mySimplify(t312)
    signals.append(t312)
    t313 = t312 ^ t309;

    t313 = mySimplify(t313)
    signals.append(t313)
    t314 = t236 & t38;

    t314 = mySimplify(t314)
    signals.append(t314)
    t315 = t237 & t39;

    t315 = mySimplify(t315)
    signals.append(t315)
    t316 = t236 & t39;

    t316 = mySimplify(t316)
    signals.append(t316)
    t317 = t237 & t38;

    t317 = mySimplify(t317)
    signals.append(t317)
    t318 = t314 ^ r0_119_16733;

    t318 = mySimplify(t318)
    signals.append(t318)
    t319 = t318 ^ t316;

    t319 = mySimplify(t319)
    signals.append(t319)
    t320 = t315 ^ r0_119_16733;

    t320 = mySimplify(t320)
    signals.append(t320)
    t321 = t320 ^ t317;

    t321 = mySimplify(t321)
    signals.append(t321)
    t322 = t240 & t8;

    t322 = mySimplify(t322)
    signals.append(t322)
    t323 = t241 & t9;

    t323 = mySimplify(t323)
    signals.append(t323)
    t324 = t240 & t9;

    t324 = mySimplify(t324)
    signals.append(t324)
    t325 = t241 & t8;

    t325 = mySimplify(t325)
    signals.append(t325)
    t326 = t322 ^ r0_120_16734;

    t326 = mySimplify(t326)
    signals.append(t326)
    t327 = t326 ^ t324;

    t327 = mySimplify(t327)
    signals.append(t327)
    t328 = t323 ^ r0_120_16734;

    t328 = mySimplify(t328)
    signals.append(t328)
    t329 = t328 ^ t325;

    t329 = mySimplify(t329)
    signals.append(t329)
    t330 = t236 & t16;

    t330 = mySimplify(t330)
    signals.append(t330)
    t331 = t237 & t17;

    t331 = mySimplify(t331)
    signals.append(t331)
    t332 = t236 & t17;

    t332 = mySimplify(t332)
    signals.append(t332)
    t333 = t237 & t16;

    t333 = mySimplify(t333)
    signals.append(t333)
    t334 = t330 ^ r0_121_16735;

    t334 = mySimplify(t334)
    signals.append(t334)
    t335 = t334 ^ t332;

    t335 = mySimplify(t335)
    signals.append(t335)
    t336 = t331 ^ r0_121_16735;

    t336 = mySimplify(t336)
    signals.append(t336)
    t337 = t336 ^ t333;

    t337 = mySimplify(t337)
    signals.append(t337)
    t338 = t188 & t22;

    t338 = mySimplify(t338)
    signals.append(t338)
    t339 = t189 & t23;

    t339 = mySimplify(t339)
    signals.append(t339)
    t340 = t188 & t23;

    t340 = mySimplify(t340)
    signals.append(t340)
    t341 = t189 & t22;

    t341 = mySimplify(t341)
    signals.append(t341)
    t342 = t338 ^ r0_122_16736;

    t342 = mySimplify(t342)
    signals.append(t342)
    t343 = t342 ^ t340;

    t343 = mySimplify(t343)
    signals.append(t343)
    t344 = t339 ^ r0_122_16736;

    t344 = mySimplify(t344)
    signals.append(t344)
    t345 = t344 ^ t341;

    t345 = mySimplify(t345)
    signals.append(t345)
    t346 = t238 & t10;

    t346 = mySimplify(t346)
    signals.append(t346)
    t347 = t239 & t11;

    t347 = mySimplify(t347)
    signals.append(t347)
    t348 = t238 & t11;

    t348 = mySimplify(t348)
    signals.append(t348)
    t349 = t239 & t10;

    t349 = mySimplify(t349)
    signals.append(t349)
    t350 = t346 ^ r0_123_16737;

    t350 = mySimplify(t350)
    signals.append(t350)
    t351 = t350 ^ t348;

    t351 = mySimplify(t351)
    signals.append(t351)
    t352 = t347 ^ r0_123_16737;

    t352 = mySimplify(t352)
    signals.append(t352)
    t353 = t352 ^ t349;

    t353 = mySimplify(t353)
    signals.append(t353)
    t354 = t188 & r_1647;

    t354 = mySimplify(t354)
    signals.append(t354)
    t355 = t189 & t7;

    t355 = mySimplify(t355)
    signals.append(t355)
    t356 = t188 & t7;

    t356 = mySimplify(t356)
    signals.append(t356)
    t357 = t189 & r_1647;

    t357 = mySimplify(t357)
    signals.append(t357)
    t358 = t354 ^ r0_124_16738;

    t358 = mySimplify(t358)
    signals.append(t358)
    t359 = t358 ^ t356;

    t359 = mySimplify(t359)
    signals.append(t359)
    t360 = t355 ^ r0_124_16738;

    t360 = mySimplify(t360)
    signals.append(t360)
    t361 = t360 ^ t357;

    t361 = mySimplify(t361)
    signals.append(t361)
    t362 = t238 & t48;

    t362 = mySimplify(t362)
    signals.append(t362)
    t363 = t239 & t49;

    t363 = mySimplify(t363)
    signals.append(t363)
    t364 = t238 & t49;

    t364 = mySimplify(t364)
    signals.append(t364)
    t365 = t239 & t48;

    t365 = mySimplify(t365)
    signals.append(t365)
    t366 = t362 ^ r0_125_16739;

    t366 = mySimplify(t366)
    signals.append(t366)
    t367 = t366 ^ t364;

    t367 = mySimplify(t367)
    signals.append(t367)
    t368 = t363 ^ r0_125_16739;

    t368 = mySimplify(t368)
    signals.append(t368)
    t369 = t368 ^ t365;

    t369 = mySimplify(t369)
    signals.append(t369)
    t370 = t303 ^ t327;

    t370 = mySimplify(t370)
    signals.append(t370)
    t371 = t305 ^ t329;

    t371 = mySimplify(t371)
    signals.append(t371)
    t372 = t271 ^ t343;

    t372 = mySimplify(t372)
    signals.append(t372)
    t373 = t273 ^ t345;

    t373 = mySimplify(t373)
    signals.append(t373)
    t374 = t229 ^ t295;

    t374 = mySimplify(t374)
    signals.append(t374)
    t375 = t231 ^ t297;

    t375 = mySimplify(t375)
    signals.append(t375)
    t376 = t263 ^ t271;

    t376 = mySimplify(t376)
    signals.append(t376)
    t377 = t265 ^ t273;

    t377 = mySimplify(t377)
    signals.append(t377)
    t378 = t359 ^ t351;

    t378 = mySimplify(t378)
    signals.append(t378)
    t379 = t361 ^ t353;

    t379 = mySimplify(t379)
    signals.append(t379)
    t380 = t359 ^ t229;

    t380 = mySimplify(t380)
    signals.append(t380)
    t381 = t361 ^ t231;

    t381 = mySimplify(t381)
    signals.append(t381)
    t382 = t311 ^ t319;

    t382 = mySimplify(t382)
    signals.append(t382)
    t383 = t313 ^ t321;

    t383 = mySimplify(t383)
    signals.append(t383)
    t384 = t247 ^ t367;

    t384 = mySimplify(t384)
    signals.append(t384)
    t385 = t249 ^ t369;

    t385 = mySimplify(t385)
    signals.append(t385)
    t386 = t287 ^ t311;

    t386 = mySimplify(t386)
    signals.append(t386)
    t387 = t289 ^ t313;

    t387 = mySimplify(t387)
    signals.append(t387)
    t388 = t327 ^ t335;

    t388 = mySimplify(t388)
    signals.append(t388)
    t389 = t329 ^ t337;

    t389 = mySimplify(t389)
    signals.append(t389)
    t390 = t351 ^ t374;

    t390 = mySimplify(t390)
    signals.append(t390)
    t391 = t353 ^ t375;

    t391 = mySimplify(t391)
    signals.append(t391)
    t392 = t378 ^ t384;

    t392 = mySimplify(t392)
    signals.append(t392)
    t393 = t379 ^ t385;

    t393 = mySimplify(t393)
    signals.append(t393)
    t394 = t279 ^ t370;

    t394 = mySimplify(t394)
    signals.append(t394)
    t395 = t281 ^ t371;

    t395 = mySimplify(t395)
    signals.append(t395)
    t396 = t367 ^ t386;

    t396 = mySimplify(t396)
    signals.append(t396)
    t397 = t369 ^ t387;

    t397 = mySimplify(t397)
    signals.append(t397)
    t398 = t370 ^ t392;

    t398 = mySimplify(t398)
    signals.append(t398)
    t399 = t371 ^ t393;

    t399 = mySimplify(t399)
    signals.append(t399)
    t400 = t201 ^ t392;

    t400 = mySimplify(t400)
    signals.append(t400)
    t401 = t203 ^ t393;

    t401 = mySimplify(t401)
    signals.append(t401)
    t402 = t382 ^ t394;

    t402 = mySimplify(t402)
    signals.append(t402)
    t403 = t383 ^ t395;

    t403 = mySimplify(t403)
    signals.append(t403)
    t404 = t376 ^ t394;

    t404 = mySimplify(t404)
    signals.append(t404)
    t405 = t377 ^ t395;

    t405 = mySimplify(t405)
    signals.append(t405)
    t406 = t279 ^ t396;

    t406 = mySimplify(t406)
    signals.append(t406)
    t407 = t281 ^ t397;

    t407 = mySimplify(t407)
    signals.append(t407)
    t408 = t400 ^ t402;

    t408 = mySimplify(t408)
    signals.append(t408)
    t409 = t401 ^ t403;

    t409 = mySimplify(t409)
    signals.append(t409)
    t410 = t255 ^ t404;

    t410 = mySimplify(t410)
    signals.append(t410)
    t411 = t257 ^ t405;

    t411 = mySimplify(t411)
    signals.append(t411)
    t412 = t396 ^ t404;

    t412 = mySimplify(t412)
    signals.append(t412)
    t413 = t397 ^ t405;

    t413 = mySimplify(t413)
    signals.append(t413)
    t414 = t390 ^ t402;

    t414 = mySimplify(t414)
    signals.append(t414)
    t415 = t391 ^ t403;

    t415 = mySimplify(t415)
    signals.append(t415)
    t416 = t374 ^ t398;

    t416 = mySimplify(t416)
    signals.append(t416)
    t417 = t375 ^ t399;

    t417 = mySimplify(t417)
    signals.append(t417)
    t418 = t406 ^ t408;

    t418 = mySimplify(t418)
    signals.append(t418)
    t419 = t407 ^ t409;

    t419 = mySimplify(t419)
    signals.append(t419)
    t420 = t384 ^ t410;

    t420 = mySimplify(t420)
    signals.append(t420)
    t421 = t385 ^ t411;

    t421 = mySimplify(t421)
    signals.append(t421)
    t422 = t380 ^ t410;

    t422 = mySimplify(t422)
    signals.append(t422)
    t423 = t381 ^ t411;

    t423 = mySimplify(t423)
    signals.append(t423)
    t424 = t372 ^ t408;

    t424 = mySimplify(t424)
    signals.append(t424)
    t425 = t373 ^ t409;

    t425 = mySimplify(t425)
    signals.append(t425)
    t426 = t406 ^ t420;

    t426 = mySimplify(t426)
    signals.append(t426)
    t427 = t407 ^ t421;

    t427 = mySimplify(t427)
    signals.append(t427)
    t428 = t388 ^ t418;

    t428 = mySimplify(t428)
    signals.append(t428)
    t429 = t389 ^ t419;

    t429 = mySimplify(t429)
    signals.append(t429)

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


