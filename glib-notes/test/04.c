//mainloop2.c
#include <glib.h>
#include <stdio.h>
#include <strings.h>

GMainLoop* loop;

//当stdin有数据可读时被GSource调用的回调函数
gboolean callback(GIOChannel *channel, GIOCondition condition, gpointer data)
{
    g_print ("aaaaaaaaaa\n");
    gchar* str;
    gsize len;
    //从stdin读取一行字符串
    g_io_channel_read_line(channel, &str, &len, NULL, NULL);
    //去掉回车键()
    while(len > 0 && (str[len-1] == '\r' || str[len-1] == '\n'))
        str[--len]='\0';
    //反转字符串
    for(;len;len--)
        g_print("%c",str[len-1]);
    g_print("\n");
    //判断结束符
    if(strcasecmp(str, "q") == 0){
        g_main_loop_quit(loop);
    }
    g_free(str);
}

void add_source(void)
{
    GIOChannel* channel;
    //这里我们监视stdin是否可读， stdin的fd默认等于1
    channel = g_io_channel_unix_new(1);
    g_io_add_watch(channel, G_IO_IN, callback, NULL);
    g_io_channel_unref(channel);
}

int main(int argc, char* argv[])
{
    GMainContext *context;
    //然后把GSource附到这个Context上
    add_source();
    //把Context赋给GMainLoop
    loop = g_main_loop_new(NULL, FALSE);

    g_print("input string('q' to quit)\n");
    g_main_loop_run(loop);

    g_main_loop_unref(loop);

    return 0;
} 
