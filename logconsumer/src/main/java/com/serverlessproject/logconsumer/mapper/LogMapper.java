package com.serverlessproject.logconsumer.mapper;

import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface LogMapper {

    void saveLog(String log);

}
