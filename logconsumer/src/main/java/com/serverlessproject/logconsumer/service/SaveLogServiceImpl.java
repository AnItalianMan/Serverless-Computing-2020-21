package com.serverlessproject.logconsumer.service;

import com.serverlessproject.logconsumer.dao.LoggerDao;

public class SaveLogServiceImpl implements SaveLogService {


    private LoggerDao loggerDao;

    public SaveLogServiceImpl(LoggerDao loggerDao) {
        this.loggerDao = loggerDao;
    }

    @Override
    public void saveLog(String log) {
        loggerDao.savelog(log);
    }
}
