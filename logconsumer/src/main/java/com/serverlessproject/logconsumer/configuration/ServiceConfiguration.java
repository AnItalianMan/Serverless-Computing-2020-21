package com.serverlessproject.logconsumer.configuration;


import com.serverlessproject.logconsumer.service.LogService;
import com.serverlessproject.logconsumer.service.LogServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ServiceConfiguration {

    @Autowired
    private DaoConfiguration daoConfiguration;

    @Bean
    public LogService logService(){
        return new LogServiceImpl(daoConfiguration.loggerDao());
    }
}
