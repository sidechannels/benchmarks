internal[2] XOR(internal[2] a, internal[2] b) {
	internal[2] res;
	res[0] = a[0] ^ b[0];
	res[1] = a[1] ^ b[1];
  	return res;
}

internal[2] XOR_pub(internal[2] a, internal b) {
	internal[2] res;
	res[0] = a[0] ^ b;
	res[1] = a[1];
	return res;
}

internal[2] gf256_xtimes(internal[2] a) {
	internal[2] res;
	int i;
  	for (i = 0; i <= 1; i = i + 1) {
  		res[i] = XTIMES a[i];
  	}
  	return res;
}

share[2] preshare(private k) {
    internal[2] x;
    random r;
    x[0] = r;
    x[1] = k ^ r;
    return x;
}

share[2] preshare_public(public a) {
    internal[2] x;
    random r;
    x[0] = r;
    x[1] = a ^ r;
    return x;
}

internal[2] power2(internal[2] x) {
    internal[2] z;
    z[0] = POW2 x[0];
    z[1] = POW2 x[1];
    return z;
}
internal[2] power4(internal[2] x) {
    internal[2] z;
    z[0] = POW4 x[0];
    z[1] = POW4 x[1];
    return z;
}
internal[2] power16(internal[2] x) {
    internal[2] z;
    z[0] = POW16 x[0];
    z[1] = POW16 x[1];
    return z;
}

internal[2] RefreshA(share[2] a) {
	internal[2] c;
    random r;
    c[0] = a[0] ^ r;
    c[1] = a[1] ^ r;
	return c;
}

internal[2] SecMult(share[2] a, share[2] b) {
	internal[2] c;
	int i;
    for(i = 0; i <= 1; i = i + 1) {
           c[i] = a[i] * b[i];
    }

    int j;
    for(i = 0; i <= 1; i = i + 1) {
        for(j = i + 1; j <= 1; j = j + 1) {
            random s;
            internal t1 = a[i] * b[j];
            internal t2 = s ^ t1;
            internal t3 = a[j] * b[i];
            internal ss = t2 ^ t3;
            c[i] = c[i] ^ s;
            c[j] = c[j] ^ ss;
        }
    }

	return c;
}

internal[2] power254(internal[2] x) {
	internal[2] z;
	internal[2] y;
	internal[2] w;
	z = power2(x);
	z = RefreshA(z);
	y = SecMult(z, x);
	w = power4(y);
	w = RefreshA(w);
	y = SecMult(y, w);
	y = power16(y);
	y = SecMult(y, w);
	y = SecMult(y, z);
	return y;
}
internal[2] sbox(internal[2] a) {
	internal[2] res;
	res = power254(a);
    for(i = 0; i <= 1; i = i + 1) {
        res[i] = AFFINE res[i];
    }
	return res;
}


internal[11][16][2] KeyExpansion(share[16][2] Key) {
    internal[11][16][2] RoundKey;
    int i;
    int j;
	for(i = 0; i <= 15; i = i + 1) {
	    for(j = 0; j <= 1; j = j + 1) {
	        RoundKey[0][i][j] = Key[i][j];
	    }
	}
	internal[4][2] temp;

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

internal[16][2] AddRoundKey(internal[16][2] st, internal[16][2] rk) {
	internal[16][2] res;
	int i;
	for(i = 0; i <= 15; i = i + 1) {
		res[i] = XOR(st[i], rk[i]);
	}
	return res;
}



internal[16][2] SubBytes(internal[16][2] st) {
	internal[16][2] res;
	int i;
	for(i = 0; i <= 15; i = i + 1) {
		res[i] = sbox(st[i]);
	}
	return res;
}

internal[16][2] ShiftRows (internal[16][2] st) {
	internal[16][2] res;
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

internal[16][2] MixColumns (internal[16][2] st) {
	internal[2] Tm01;
	internal[2] Tm01p;
	internal[2] Tm12;
	internal[2] Tm12p;
	internal[2] Tm23;
	internal[2] Tm23p;
	internal[2] Tm30;
	internal[2] Tm30p;
	internal[2] Tmp;

	internal[16][2] res;
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


share[16][2] Cipher(share[16][2] State, share[16][2] Key) {
	internal[11][16][2] RoundKey;
	RoundKey = KeyExpansion(Key);

	internal[16][2] st = AddRoundKey(State, RoundKey[0]);
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
    internal[16][2] Key;
    internal[16][2] State;

    #int i;
	#for(i = 0; i <= 15; i = i + 1) {
	#	Key[i] = preshare(k[i]);
	#	State[i] = preshare_public(plaintext[i]);
	#}
	Key[0] = preshare(k[0]);
    State[0] = preshare_public(plaintext[0]);
    Key[1] = preshare(k[1]);
    State[1] = preshare_public(plaintext[1]);
    Key[2] = preshare(k[2]);
    State[2] = preshare_public(plaintext[2]);
    Key[3] = preshare(k[3]);
    State[3] = preshare_public(plaintext[3]);
    Key[4] = preshare(k[4]);
    State[4] = preshare_public(plaintext[4]);
    Key[5] = preshare(k[5]);
    State[5] = preshare_public(plaintext[5]);
    Key[6] = preshare(k[6]);
    State[6] = preshare_public(plaintext[6]);
    Key[7] = preshare(k[7]);
    State[7] = preshare_public(plaintext[7]);
    Key[8] = preshare(k[8]);
    State[8] = preshare_public(plaintext[8]);
    Key[9] = preshare(k[9]);
    State[9] = preshare_public(plaintext[9]);
    Key[10] = preshare(k[10]);
    State[10] = preshare_public(plaintext[10]);
    Key[11] = preshare(k[11]);
    State[11] = preshare_public(plaintext[11]);
    Key[12] = preshare(k[12]);
    State[12] = preshare_public(plaintext[12]);

    Key[13] = preshare(k[13]);
    State[13] = preshare_public(plaintext[13]);
    Key[14] = preshare(k[14]);
    State[14] = preshare_public(plaintext[14]);
    Key[15] = preshare(k[15]);
    State[15] = preshare_public(plaintext[15]);

	internal[16][2] res = Cipher(State, Key);

}

