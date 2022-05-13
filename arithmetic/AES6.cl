internal[3] XOR(internal[3] a, internal[3] b) {
	internal[3] res;
	res[0] = a[0] ^ b[0];
	res[1] = a[1] ^ b[1];
	res[2] = a[2] ^ b[2];
  	return res;
}

internal[3] XOR_pub(internal[3] a, internal b) {
	internal[3] res;
	res[0] = a[0] ^ b;
	res[1] = a[1];
	res[2] = a[2];
	return res;
}

internal[3] gf256_xtimes(internal[3] a) {
	internal[3] res;
	int i;
  	for (i = 0; i <= 2; i = i + 1) {
  		res[i] = XTIMES a[i];
  	}
  	return res;
}

share[3] preshare(private k) {
    internal[3] x;
    random r;
    random r1;
    x[0] = r;
    x[1] = r1;
    x[2] = k ^ r ^ r1;
    return x;
}

share[3] preshare_public(public a) {
    internal[3] x;
    random r;
    random r1;
    x[0] = r;
    x[1] = r1;
    x[2] = a ^ r ^ r1;
    return x;
}

internal[3] RefreshA(share[3] a) {
	internal[3] c;
    c[0] = a[0];
	int i;
	for(i = 1; i <= 2; i = i + 1) {
	    random r;
	    c[0] = c[0] ^ r;
	    c[i] = a[i] ^ r;
	}
	return c;
}

internal[3] power2(internal[3] x) {
    internal[3] z;
    z[0] = POW2 x[0];
    z[1] = POW2 x[1];
    z[2] = POW2 x[2];
    return z;
}
internal[3] power4(internal[3] x) {
    internal[3] z;
    z[0] = POW4 x[0];
    z[1] = POW4 x[1];
    z[2] = POW4 x[2];
    return z;
}
internal[3] power16(internal[3] x) {
    internal[3] z;
    z[0] = POW16 x[0];
    z[1] = POW16 x[1];
    z[2] = POW16 x[2];
    return z;
}

internal[3] SecMult_RP10(share[3] a, share[3] b) {
	internal[3] c;
    int i;
    int j;
    internal[3][3] r;
    for(i = 0; i <= 2; i = i + 1) {
        for(j = i + 1; j <= 2; j = j + 1) {
            random s;
            r[i][j] = s;
            r[j][i] = r[i][j] ^ (a[i] * b[j]) ^ (a[j] * b[i]);
        }
    }


    c[0] = a[0] * b[0];
    c[0] = c[0] ^ r[0][1];
    c[0] = c[0] ^ r[0][2];

    c[1] = a[1] * b[1];
    c[1] = c[1] ^ r[1][0];
    c[1] = c[1] ^ r[1][2];

    c[2] = a[2] * b[2];
    c[2] = c[2] ^ r[2][0];
    c[2] = c[2] ^ r[2][1];

    return c;
}

internal[3] power254(internal[3] x) {
	internal[3] z;
	internal[3] y;
	internal[3] w;
	z = power2(x);
	z = RefreshA(z);
	y = SecMult_RP10(z, x);
	w = power4(y);
	w = RefreshA(w);
	y = SecMult_RP10(y, w);
	y = power16(y);
	y = SecMult_RP10(y, w);
	y = SecMult_RP10(y, z);
	return y;
}
internal[3] sbox(internal[3] a) {
	internal[3] res;
	res = power254(a);
	int i;
    for(i = 0; i <= 2; i = i + 1) {
        res[i] = AFFINE res[i];
    }
	return res;
}


internal[11][16][3] KeyExpansion(share[16][3] Key) {
    internal[11][16][3] RoundKey;
    int i;
    int j;
	for(i = 0; i <= 15; i = i + 1) {
	    for(j = 0; j <= 2; j = j + 1) {
	        RoundKey[0][i][j] = Key[i][j];
	    }
	}
	internal[4][3] temp;

	for(i = 1; i <= 10; i = i + 1) {
		temp[0] = sbox(RoundKey[i - 1][13]);
		temp[1] = sbox(RoundKey[i - 1][14]);
		temp[2] = sbox(RoundKey[i - 1][15]);
		temp[3] = sbox(RoundKey[i - 1][12]);
		internal r = RCON i;
		temp[0] = XOR_pub(temp[0], r);

		RoundKey[i][0] = XOR(RoundKey[i - 1][0], temp[0]);
		RoundKey[i][1] = XOR(RoundKey[i - 1][1], temp[1]);
		RoundKey[i][2] = XOR(RoundKey[i - 1][2], temp[2]);
		RoundKey[i][3] = XOR(RoundKey[i - 1][3], temp[3]);

		for(j = 1; j <= 3; j = j + 1) {
			RoundKey[i][(j * 4) + 0] = XOR(RoundKey[i - 1][(j * 4) + 0], RoundKey[i][(j - 1) * 4 + 0]);
			RoundKey[i][(j * 4) + 1] = XOR(RoundKey[i - 1][(j * 4) + 1], RoundKey[i][(j - 1) * 4 + 1]);
			RoundKey[i][(j * 4) + 2] = XOR(RoundKey[i - 1][(j * 4) + 2], RoundKey[i][(j - 1) * 4 + 2]);
			RoundKey[i][(j * 4) + 3] = XOR(RoundKey[i - 1][(j * 4) + 3], RoundKey[i][(j - 1) * 4 + 3]);
		}

	}

	return RoundKey;
}

internal[16][3] AddRoundKey(internal[16][3] st, internal[16][3] rk) {
	internal[16][3] res;
	int i;
	for(i = 0; i <= 15; i = i + 1) {
		res[i] = XOR(st[i], rk[i]);
	}

	return res;
}



internal[16][3] SubBytes(internal[16][3] st) {
	internal[16][3] res;
	int i;
	for(i = 0; i <= 15; i = i + 1) {
		res[i] = sbox(st[i]);
	}
	return res;
}

internal[16][3] ShiftRows (internal[16][3] st) {
	internal[16][3] res;
	res[1] = st[5];
	res[5] = st[9];
	res[9] = st[13];
	res[13] = st[1];
	res[2] = st[10];
	res[10] = st[2];
	res[6] = st[14];
	res[14] = st[6];
	res[15] = st[11];
	res[11] = st[7];
	res[7] = st[3];
	res[3] = st[15];

	res[0] = st[0];
	res[4] = st[4];
	res[8] = st[8];
	res[12] = st[12];

	return res;

}

internal[16][3] MixColumns (internal[16][3] st) {
	internal[3] Tm01;
	internal[3] Tm01p;
	internal[3] Tm12;
	internal[3] Tm12p;
	internal[3] Tm23;
	internal[3] Tm23p;
	internal[3] Tm30;
	internal[3] Tm30p;
	internal[3] Tmp;

	internal[16][3] res;
	int i;

	for(i = 0; i <= 3; i = i + 1) {
	    Tm01 = XOR(st[i * 4], st[(i * 4) + 1]);
	    Tm12 = XOR(st[(i * 4) + 1], st[(i * 4) + 2]);
	    Tm23 = XOR(st[(i * 4) + 2], st[(i * 4) + 3]);
	    Tm30 = XOR(st[(i * 4) + 3], st[i * 4]);
	    Tmp = XOR(Tm01, Tm23);
	    Tm01p = gf256_xtimes(Tm01);
	    res[i * 4] = XOR(st[i * 4], Tm01p);
	    res[i * 4] = XOR(res[i * 4], Tmp);
	    Tm12p = gf256_xtimes(Tm12);
	    res[(i * 4) + 1] = XOR(st[(i * 4) + 1], Tm12p);
	    res[(i * 4) + 1] = XOR(res[(i * 4) + 1], Tmp);
	    Tm23p = gf256_xtimes(Tm23);
	    res[(i * 4) + 2] = XOR(st[(i * 4) + 2], Tm23p);
	    res[(i * 4) + 2] = XOR(res[(i * 4) + 2], Tmp);
	    Tm30p = gf256_xtimes(Tm30);
	    res[(i * 4) + 3] = XOR(st[(i * 4) + 3], Tm30p);
	    res[(i * 4) + 3] = XOR(res[(i * 4) + 3], Tmp);
	}

	return res;
}


share[16][3] Cipher(share[16][3] State, share[16][3] Key) {
	internal[11][16][3] RoundKey;
	RoundKey = KeyExpansion(Key);

	internal[16][3] st = AddRoundKey(State, RoundKey[0]);
    int i;
    for(i = 1; i <= 9; i = i + 1) {
        st = SubBytes(st);
        st = ShiftRows(st);
        st = MixColumns(st);
        st = AddRoundKey(st, RoundKey[i]);
    }

    st = SubBytes(st);
    st = ShiftRows(st);
    st = AddRoundKey(st, RoundKey[10]);

    return st;
}

void main(private[16] k, public[16] plaintext) {
    internal[16][3] Key;
    internal[16][3] State;

    int i;
	for(i = 0; i <= 15; i = i + 1) {
		Key[i] = preshare(k[i]);
		State[i] = preshare_public(plaintext[i]);
	}

	internal[16][3] res = Cipher(State, Key);

}

