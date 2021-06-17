package com.serverlessproject.logconsumer.configuration;

import com.serverlessproject.logconsumer.dao.LoggerDao;
import com.serverlessproject.logconsumer.dao.LoggerDaoImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DaoConfiguration {

    @Bean
    public LoggerDao loggerDao() {
        return new LoggerDaoImpl();
    }

}
