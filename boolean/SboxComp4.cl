
n = 5;
share[n] preshare(private k) {
	share[n] x;
	x[n - 1] = k;
    for (i = 0; i <= n - 2; i = i + 1){
        random r;
        x[i] = r;
        x[n - 1] = x[n - 1] ^ r;
    }
    return x;
}
internal[5] compression(internal[5] a, internal[5] b) {
    random r0;
    random r1;
    random r2;
    random r3;
    random r4;
    internal t1 = a[0] * b[0];
    internal t2 = a[0] * b[1];
    internal t3 = a[1] * b[0];
    internal t4 = a[0] * b[2];
    internal t5 = a[2] * b[0];
    internal t6 = a[1] * b[1];
    internal t7 = a[1] * b[2];
    internal t8 = a[2] * b[1];
    internal t9 = a[1] * b[3];
    internal t10 = a[3] * b[1];
    internal t11 = a[2] * b[2];
    internal t12 = a[2] * b[3];
    internal t13 = a[3] * b[2];
    internal t14 = a[2] * b[4];
    internal t15 = a[4] * b[2];
    internal t16 = a[3] * b[3];
    internal t17 = a[3] * b[4];
    internal t18 = a[4] * b[3];
    internal t19 = a[3] * b[0];
    internal t20 = a[0] * b[3];
    internal t21 = a[4] * b[4];
    internal t22 = a[4] * b[0];
    internal t23 = a[0] * b[4];
    internal t24 = a[4] * b[1];
    internal t25 = a[1] * b[4];

    internal t26 = t1 ^ r0 ^ t2 ^ t3 ^ r1 ^ t4 ^ t5;
    internal t27 = t6 ^ r1 ^ t7 ^ t8 ^ r2 ^ t9 ^ t10;
    internal t28 = t11 ^ r2 ^ t12 ^ t13 ^ r3 ^ t14 ^ t15;
    internal t29 = t16 ^ r3 ^ t17 ^ t18 ^ r4 ^ t19 ^ t20;
    internal t30 = t21 ^ r4 ^ t22 ^ t23 ^ r0 ^ t24 ^ t25;

    internal[5] res;
    res[0] = t26;
    res[1] = t27;
    res[2] = t28;
    res[3] = t29;
    res[4] = t30;

    return res;
}

internal[n] XOR(internal[n] a, internal[n] b) {
	internal[n] res;
	int i;
  	for (i = 0; i <= n - 1; i = i + 1) {
  		res[i] = a[i] ^ b[i];
  	}
  	return res;
}

internal[n] sboxbit(internal[8][n] a) {
   internal t8 = XOR(a[3], a[5]);
   internal t9 = XOR(a[0], a[6]);
   internal t10 = XOR(t9, t8);
   internal t11 = XOR(a[0], a[3]);
   internal t12 = XOR(a[0], a[5]);
   internal t13 = XOR(a[1], a[2]);
   internal t14 = XOR(t13, a[7]);
   internal t15 = XOR(t14, a[3]);
   internal t16 = XOR(t14, a[0]);
   internal t17 = XOR(t14, a[6]);
   internal t18 = XOR(a[4], t10);
   internal t19 = XOR(t17, t12);
   internal t20 = XOR(t18, a[5]);
   internal t21 = XOR(t18, a[1]);
   internal t22 = XOR(t20, a[7]);
   internal t23 = XOR(t20, t13);
   internal t24 = XOR(t21, t11);
   internal t25 = XOR(a[7], t24);
   internal t26 = XOR(t23, t24);
   internal t27 = XOR(t23, t12);
   internal t28 = XOR(t13, t24);
   internal t29 = XOR(t9, t28);
   internal t30 = XOR(a[0], t28);
   internal t31 = compression(t10, t20);
   internal t32 = compression(t19, t22);
   internal t33 = compression(t15, a[7]);
   internal t34 = compression(t9, t28);
   internal t35 = compression(t17, t14);
   internal t36 = compression(t16, t25);
   internal t37 = compression(t11, t24);
   internal t38 = compression(t8, t26);
   internal t39 = XOR(t32, t31);
   internal t40 = XOR(t33, t31);
   internal t41 = XOR(t35, t34);
   internal t42 = XOR(t36, t34);
   internal t43 = XOR(t38, t37);
   internal t44 = XOR(t39, t43);
   internal t45 = XOR(t41, t43);
   internal t46 = XOR(t44, t21);
   internal t47 = XOR(t45, t29);
   internal t48 = compression(t12, t23);
   internal t49 = compression(t46, t47);
   internal t50 = XOR(t48, t37);
   internal t51 = XOR(t40, t50);
   internal t52 = XOR(t42, t50);
   internal t53 = XOR(t52, t30);
   internal t54 = XOR(t47, t53);
   internal t55 = XOR(t51, t27);
   internal t56 = XOR(t46, t55);
   internal t57 = XOR(t53, t49);
   internal t58 = XOR(t55, t49);
   internal t59 = compression(t56, t57);
   internal t60 = compression(t58, t54);
   internal t61 = XOR(t59, t55);
   internal t62 = XOR(t60, t53);
   internal t63 = XOR(t47, t62);
   internal t64 = XOR(t57, t62);
   internal t65 = XOR(t61, t62);
   internal t66 = compression(t61, t16);
   internal t67 = compression(t53, t64);
   internal t68 = XOR(t67, t63);
   internal t69 = XOR(t57, t67);
   internal t70 = compression(t61, t69);
   internal t71 = compression(t61, t25);
   internal t72 = XOR(t62, t68);
   internal t73 = XOR(t56, t70);
   internal t74 = XOR(t73, t68);
   internal t75 = XOR(t61, t73);
   internal t76 = XOR(t65, t74);
   internal t77 = compression(t72, t20);
   internal t78 = compression(t68, t22);
   internal t79 = compression(t72, t10);
   internal t80 = compression(t68, t19);
   internal t81 = compression(t73, t14);
   internal t82 = compression(t65, t24);
   internal t83 = compression(t73, t17);
   internal t84 = compression(t65, t11);
   internal t85 = compression(t76, t26);
   internal t86 = compression(t74, t23);
   internal t87 = compression(t76, t8);
   internal t88 = compression(t74, t12);
   internal t89 = compression(t62, t15);
   internal t90 = compression(t75, t9);
   internal t91 = compression(t62, a[7]);
   internal t92 = compression(t75, t28);
   internal t93 = XOR(t84, t87);
   internal t94 = XOR(t80, t89);
   internal t95 = XOR(t71, t83);
   internal t96 = XOR(t79, t80);
   internal t97 = XOR(t91, t90);
   internal t98 = XOR(t91, t71);
   internal t99 = XOR(t85, t86);
   internal t100 = XOR(t77, t92);
   internal t101 = XOR(t82, t85);
   internal t102 = XOR(t87, t88);
   internal t103 = XOR(t90, t95);
   internal t104 = XOR(t97, t100);
   internal t105 = XOR(t81, t93);
   internal t106 = XOR(t92, t101);
   internal t107 = XOR(t93, t104);
   internal t108 = XOR(t66, t104);
   internal t109 = XOR(t99, t105);
   internal t110 = XOR(t96, t105);
   internal t111 = XOR(t81, t106);
   internal t112 = XOR(t108, t109);
   internal t113 = XOR(t78, t110);
   internal t114 = XOR(t106, t110);
   internal t115 = XOR(t103, t109);
   internal t116 = XOR(t95, t107);
   internal t117 = XOR(t111, t112);
   internal t118 = XOR(t100, t113);
   internal t119 = XOR(t98, t113);
   internal t120 = XOR(t94, t112);
   internal t121 = XOR(t111, t118);
   internal t122 = XOR(t102, t117);

   return t122;

}

internal main(private[8] k) {
    internal[8][n] Key;
    for(i = 0; i <= 7; i = i + 1) {
        Key[i] = preshare(k[i]);
    }
    internal[5] res;
    res = sboxbit(Key);
    return res;
}
