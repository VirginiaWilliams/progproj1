/**********************************************************************
 * Virginia Williams
 * 10/15/2021
 * Program to determine the key used in a aes-128-cbc encrypted file given plain text, cipher text, IV, and the fact that the ket is a less than 16 character English word.
 * Sources used:
 * https://medium.com/@amit.kulkarni/encrypting-decrypting-a-file-using-openssl-evp-b26e0e4d28d4
 * *******************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>


int encrypt(int do_encrypt) {
    // create the key and iv
    unsigned char key[] = "0123456789abcdeF";
    unsigned char iv[] = "1234567887654321";

    // Check the lengths of the key and iv before setting them
    ctx = EVP_CIPHER_CTX_new(); //ctx is a new cipher context
    EVP_CipherInit_ex2(ctx, EVP_aes_128_cbc(), NULL, NULL, do_encrypt, NULL);
    OPENSSL_assert(EVP_CIPHER_CTX_get_key_length(ctx) == 16);
    OPENSSL_assert(EVP_CIPHER_CTX_get_iv_length(ctx) == 16);

    // Now we set the values I guess
    EVP_CipherInit_ex2(ctx, NULL, key, iv, do_encrypt, NULL);




    EVP_CIPHER_CTX_free(ctx);
    return 0;
}


// ./findKey plaintext enc dec words
int main(int argc, char* argv[]) {
    File *f_words, *f_input, *f_enc, *f_dec;

    if (argc != 2) {
        printf("need words");
        return -1;
    }

    unsigned char key[] = "0123456789abcdeF";
    unsigned char iv[] = "1234567887654321";
    unsigned int encrypt = 1;
    const EVP_CIPHER * cypherType EVP_aes_128_cbc();

    // open input file
    f_input = fopen(argv[1], "rb");
    if (!f_input) {
        fprintf(stderr, "ERROR: fopen error: %s\n", strerror(errno));
        return errno;
    }

    /* Open and truncate file to zero length or create ciphertext file for writing */
    f_enc = fopen("encrypted_file", "wb");
    if (!f_enc) {
         /* Unable to open file for writing */
        fprintf(stderr, "ERROR: fopen error: %s\n", strerror(errno));
        return errno;
    }

    //encrypt the file
    enc_dec(key, iv, encrypt, cypherType, f_input, f_enc);

    //close files
    fclose(f_input);
    fclose(f_enc);


    //decrypt down here (not yet)

    return 0;
}
