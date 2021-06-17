package com.serverlessproject.logconsumer.dao;

import com.serverlessproject.logconsumer.mapper.LogMapper;
import org.springframework.beans.factory.annotation.Autowired;

public class LoggerDaoImpl implements LoggerDao {

    @Autowired
    private LogMapper logMapper;

    public LoggerDaoImpl() {
    }

    @Override
    public void savelog(String log) {
        logMapper.saveLog(log);
    }
}
