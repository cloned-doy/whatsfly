#ifndef WAPP_H
#define WAPP_H

#ifdef __cplusplus
extern "C" {
#endif

void Connect(char* number);
int SendMessage(char* number,char* msg);

#ifdef __cplusplus
}
#endif

#endif // WAPP_H
