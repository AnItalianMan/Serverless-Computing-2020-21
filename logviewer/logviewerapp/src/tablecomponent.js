import React, {useState} from 'react'
import {  Button } from 'antd'
import { Row, Col } from 'antd'
import { Table} from 'antd'

function TableComponent(props){
    
    const [logs, setLogs] = useState([])
    const [loading, setLoading] = useState(false)
    

    const columns = [
        {
            title: 'Logs',
            dataIndex: 'logs',
            render: (text, record, index) => record
        }
    ]

    const ottieniDati = async () => {
        setLoading(true)
        let response = await fetch('http://localhost:7052/getlogs');
        let data = await response.json()
        setLogs(data)
        setLoading(false)
    } 

    return (
        <>
        <Row gutter={[0,30]}>
            <Col>
                <Button type="primary" onClick={ottieniDati}>Ricarica log</Button>
            </Col>
        </Row>
        <Row>
            <Col span={24}>
                <Table dataSource={logs} columns={columns} loading={loading}/>
            </Col>
        </Row>
        
        </>
    );

}

export default TableComponent;
