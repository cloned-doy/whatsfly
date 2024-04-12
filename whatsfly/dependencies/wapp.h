#ifndef WAPP_H
#define WAPP_H

#include <stdlib.h>
#include <stdbool.h>

typedef void (*ptr_to_pyfunc_str) (char*);

static inline void call_c_func_str(ptr_to_pyfunc_str ptr, char* jsonStr) {
  (ptr)(jsonStr);
}

typedef void (*ptr_to_pyfunc) ();

static inline void call_c_func(ptr_to_pyfunc ptr) {
  (ptr)();
}

#ifdef __cplusplus
extern "C" {
#endif

  extern int NewWhatsAppClientWrapper(char* c_phone_number, char* c_media_path, ptr_to_pyfunc fn_disconnect_callback, ptr_to_pyfunc_str fn_event_callback);
  extern void ConnectWrapper(int id);
  extern void DisconnectWrapper(int id);
  extern void MessageThreadWrapper(int id);
  extern int SendMessageWrapper(int id, char* c_number, char* c_msg, bool is_group);
  extern int SendImageWrapper(int id, char* c_number, char* c_image_path, char* c_caption, bool is_group);
  
#ifdef __cplusplus
}
#endif

#endif // WAPP_H
