#include <stdio.h>
#include <cstdio>
#include <string>
#include "CLIManager.h"


std::string executeCommand(const char *command)
{
    std::string result;
    FILE *pipe = popen(command, "r");
    if (pipe)
    {
        char buffer[128];
        while (!feof(pipe))
        {
            if (fgets(buffer, 128, pipe) != nullptr)
                result += buffer;
        }
        pclose(pipe);
    }
    return result;
}
