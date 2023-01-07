## fscanf 

```c
		// fscanf 返回值:
        // 成功返回匹配结果
        // 错误或读到文件末尾返回EOF
        // int ferror( FILE *stream )
        // ferror函数的功能就是判断使用某一文件指针的过程中，是否发生错误，
        // 若使用时没有发生错误，则ferror函数返回0；否则，ferror函数将返回一个非零的值。
        // 调用ferror函数时，我们只需将待检查的文件指针传入即可。
        // int feof( FILE *stream );
        // ferror函数的功能就是判断使用某一文件指针的过程中，是否发生错误，若使用时没有发生错误，
        // 则ferror函数返回0；否则，ferror函数将返回一个非零的值。
        // 调用ferror函数时，我们只需将待检查的文件指针传入即可。

	// scanf遇上空格或\n就会结束字符串输入 %[^\n]代表遇上\n才结束字符串的读取
	ret = fscanf(fp, "%d %d %d %d %[^\n]", &a, &b, &c, &d, s);
    printf("%d-%d-%d-%d-%s\n", a, b, c, ret, s);
```

```
config
3 0 0 -1 date >> log
```

```bash
pandapirate@DESKTOP-U4GMN51:~/work/tell_time$ gcc test.c -o test
pandapirate@DESKTOP-U4GMN51:~/work/tell_time$ ./test
3-0-0-5-date >> log
```

