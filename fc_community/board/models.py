from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=128, 
                                verbose_name='title')
    contents = models.TextField(verbose_name='contents')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                                verbose_name='writer') # CASCADE, SET_NULL, SET_DEFAULT... 
    tags = models.ManyToManyField('tag.Tag', verbose_name='tag')
    registered_dttm = models.DateTimeField(auto_now_add=True, 
                                verbose_name='registered_time')
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fccommunity_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'
        