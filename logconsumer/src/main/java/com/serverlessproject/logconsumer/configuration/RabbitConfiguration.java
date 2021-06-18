package com.serverlessproject.logconsumer.configuration;

import com.serverlessproject.logconsumer.component.RabbitLogListener;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.amqp.core.Queue;

@Configuration
public class RabbitConfiguration {

    @Value("${rabbit.user.username}")
    private String username;

    @Value("${rabbit.user.password}")
    private String password;

    @Value("${rabbit.queue.name}")
    private String queueName;

    @Autowired
    private ServiceConfiguration serviceConfiguration;

    @Bean
    public RabbitLogListener rabbitLogListener(){
        return new RabbitLogListener(serviceConfiguration.logService());
    }

    @Bean
    public ConnectionFactory pooledConnectionFactory() {
        CachingConnectionFactory cachingConnectionFactory = new CachingConnectionFactory();
        cachingConnectionFactory.setUsername(username);
        cachingConnectionFactory.setPassword(password);
        return cachingConnectionFactory;
    }

    @Bean
    public Queue queue(){
        return new Queue(queueName, false);
    }


}
