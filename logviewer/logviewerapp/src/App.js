import React from 'react';
import './App.css';
import 'antd/dist/antd.css';
import './index.css';
import { Layout } from 'antd';
import {
  CloudServerOutlined,
} from '@ant-design/icons';
import TableComponent from './tablecomponent';
const { Header, Content, Footer } = Layout;


function App() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <div className="logo" />
        <Layout className="site-layout">
          <Header className="site-layout-background" style={{ padding: 0 }} />
          <Content style={{ margin: '0 16px' }}>
            <div className="site-layout-background" style={{ padding: 24, minHeight: 360 }}>
              <TableComponent/>
            </div>
          </Content>
          <Footer style={{ textAlign: 'center' }}>Serverless project ©2021</Footer>
        </Layout>
      </Layout>
  );
}

export default App;
