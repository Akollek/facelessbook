/* auth.c
 * ------
 *  Author : Amiel Kollek
 *  Purpose: Simple authentication for facelessbook
 */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>


void printHTML(int key, char username[]){
        printf("<DOCTYPE html>\n");
        printf("");
        printf("<html>\n");
        printf("        <body>\n");
        printf("                <p> Thank you for logging in. Please click below to proceed to your newsfeed</p>\n");
        printf("                <form action=\"cgi-bin/newsfeed/newsfeed.py\" method=\"post\">\n");
        printf("                        <input type=\"submit\" value=\"Newsfeed\">\n");
        printf("                        <input type=\"hidden\" value=\"%s\">\n", username);
        printf("                        <input type=\"hidden\" value=\"%d\">\n", key);
        printf("                </form>\n");
        printf("        </body>\n");
        printf("</html>\n");
}


int main(void){
        // set rand seed with time
        srand(time(0));

        char * username = "bob";
         // generate a random key
        int key = rand();
        FILE * keyfile;
        char keyfilepath[20 + 10]; // max username + extra for "keys/[...].key\0"

        // generate a filename for the key of this user
        snprintf(keyfilepath, sizeof(keyfilepath), "%s%s%s", "keys/", username, ".key\0");

        // open the keyfile ("w" option destroys contenst if the file exists already 
        keyfile = fopen(keyfilepath,"w");

        // write the key to the file and close
        fprintf(keyfile, "%d", key);
        fclose(keyfile);
        printHTML(key,username); 

        return 0;
}
