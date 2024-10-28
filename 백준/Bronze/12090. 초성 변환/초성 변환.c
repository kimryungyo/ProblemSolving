#include <stdio.h>

void printChar(int ascii) {
    unsigned int a, b, c, d;
    d = ascii % 256;
    ascii >>= 8;
    c = ascii % 256;
    ascii >>= 8;
    b = ascii % 256;
    ascii >>= 8;
    a = ascii % 256;

    if (a != 0) { printf("%c", a); }
    if (b != 0) { printf("%c", b); }
    if (c != 0) { printf("%c", c); }
    if (d != 0) { printf("%c", d); }
}

int charToBinary(char c) {
    unsigned int binary = 0;
    for (int i = 7; i >= 0; i--) {
        binary = (binary << 1) | ((c >> i) & 1);
    }
    return binary;
}
    
int main() {
    unsigned int range[19] = { 15380608, 15382924, 15434392, 15436708, 15439024, 15441340, 15443848, 15446164, 15448480, 15499948, 15502264, 15504772, 15507088, 15509404, 15511720, 15514036, 15565696, 15568012, 15570328 };
    unsigned int values[19] = { 14910641, 14910642, 14910644, 14910647, 14910648, 14910649, 14910849, 14910850, 14910851, 14910853, 14910854, 14910855, 14910856, 14910857, 14910858, 14910859, 14910860, 14910861, 14910862 };

    char inputs[333];
    scanf("%s", inputs);
    
    unsigned int byte, ch, len;
    unsigned int answer, idx;

    idx = 0;
    while (1) {

        if (inputs[idx] == '\0') {
            break;
        } 
        
        byte = charToBinary(inputs[idx]);
        
        if ((byte & 0b11100000) == 0b11000000) {
            len = 2;
        } else if ((byte & 0b11110000) == 0b11100000) {
            len = 3;
        } else {
            len = 0;
        }
        
        ch = byte;
        for (int j = 0; j < len - 1; j++) {
            idx++;
            ch <<= 8;
            byte = charToBinary(inputs[idx]);
            ch += byte;
        }
        
        for (int j = 0; j < 19; j++) {
            if (ch >= range[j]) {
                answer = values[j];
            }
        }

        printChar(answer);
        idx++;
    }

    printf("\n");
    return 0;
}