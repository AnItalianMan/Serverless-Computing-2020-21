package com.serverlessproject.logconsumer.service;

import com.serverlessproject.logconsumer.dao.LoggerDao;

import java.util.Collections;
import java.util.List;

public class LogServiceImpl implements LogService {


    private LoggerDao loggerDao;

    public LogServiceImpl(LoggerDao loggerDao) {
        this.loggerDao = loggerDao;
    }

    @Override
    public void saveLog(String log) {
        loggerDao.savelog(log);
    }

    @Override
    public List<String> getLogs() {
        List<String> logs = loggerDao.retreiveLogs();
        if (logs.size() == 0){
            return Collections.singletonList("No logs found");
        }else{
            return logs;
        }
    }
}
