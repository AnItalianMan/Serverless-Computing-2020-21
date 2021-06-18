package com.serverlessproject.logconsumer.mapper;

import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface LogMapper {

    void saveLog(String log);

    List<String> retreiveLogs();
}
