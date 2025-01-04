#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to get the SubTexture details from XML file
typedef struct {
    char name[256];
    int x, y;
    int width, height;
} SubTexture;

SubTexture* parse_texture_atlas(char* filename) {
    // Open the XML file for reading
    FILE* xmlfile = fopen(filename, "r");
    if (!xmlfile) {
        printf("Error opening file\n");
        exit(1);
    }

    char line[1024];
    SubTexture* textures = NULL;
    int num_textures = 0;

    while (fgets(line, sizeof(line), xmlfile)) {
        // Check if the line contains a <SubTexture> element
        if (strncmp(line, "<SubTexture", 11) == 0) {
            char attribute[256];
            int x, y;
            int width, height;

            sscanf(line, "<SubTexture name=\"%[^\"]\" x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\"/>",
                   attribute, &x, &y, &width, &height);

            num_textures++;
            textures = realloc(textures, num_textures * sizeof(SubTexture));
            strcpy(textures[num_textures - 1].name, attribute);
            textures[num_textures - 1].x = x;
            textures[num_textures - 1].y = y;
            textures[num_textures - 1].width = width;
            textures[num_textures - 1].height = height;
        }
    }

    fclose(xmlfile);

    if (!textures) {
        printf("Error parsing XML file\n");
        exit(1);
    }

    return textures;
}

int main() {
    char filename[] = "simpleSpace_sheet.xml";
    SubTexture* textures = parse_texture_atlas(filename);

    for (int i = 0; i < strlen(textures[0].name); i++) {
        if (textures[i].name[i] == '.') {
            printf("%s\n", textures[i].name);
        }
    }

    // Free memory allocated by the function
    free(textures);

    return 0;
}
