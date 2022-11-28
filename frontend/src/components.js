import React, { useState, useEffect, useRef } from "react";
import {Divider, Form, Select, Input, InputNumber, Button, Checkbox, Space, message } from 'antd';
import { PlusOutlined } from '@ant-design/icons';
let index = 0;
export function AccountForm ({accounts}) {
    const [formResponse, setFormResponse] = useState([]);
    const [messageApi, contextHolder] = message.useMessage();
    const [items, setItems] = useState(['jack', 'lucy']);
    const [name, setName] = useState('');
    const inputRef = useRef(null);
    /**
     * submits params to execute a transition
     * @param {object} values {sender receiver parivate_key amount}
     * @return {object}  {status, message}
     */
    function onFinish (values) {
        fetch('/api/register', {method: 'POST', header: { 'Content-Type': 'application/json' }, body:JSON.stringify(values)})
            .then(response => response.json().then(setFormResponse))
        messageApi.open({
          type: formResponse.status,
          content: formResponse.message,
        });
    }
    const form = Form.useForm();
    const options = [
      { label: 'Apple', value: 'Apple' },
      { label: 'Pear', value: 'Pear' },
      { label: 'Orange', value: 'Orange' },
    ];
    function onReset() {
        form.resetFields();
    }
    function onNameChange(e) {
        setName(e.target.value);
    }
    function addItem (e) {
        e.preventDefault();
        setItems([...items, name || 'item' + index++]);
        console.log(items);
        setName('');
        setTimeout(() => {
          inputRef.current?.focus();
        }, 0);
    }
    return (
        <>
            {contextHolder}
            <Form
              name="transition"
              autoComplete="off"
              layout="vertical"
              onFinish={onFinish}
            >
                <Form.Item
                    label="Sender's account"
                    name="sender"
                    rules={[{ required: true, message: 'Please choose an account' }]}
                >
                    <Select placeholder="Please choose an account">
                        {accounts.map((account) => (
                          <Select.Option key={account} value={account}>{account}</Select.Option>
                        ))}
                    </Select>
                </Form.Item>
                <Form.Item label="Sender's private key" >
                    <Input.Group compact>
                        <Form.Item
                            name="private_key"
                            noStyle
                            rules={[{ required: true, message: 'Private key is required' }]}
                        >
                            <Input style={{ width: 'calc(100% - 200px)' }} placeholder="Please input the private key" />
                        </Form.Item>
                        <Form.Item
                            name="amount"
                            noStyle
                            rules={[{ required: true, message: 'Amout is required' }]}
                        >
                            <InputNumber style={{ width: '200px' }} min={1} max={10} keyboard={true} placeholder="Please input the amount" />
                        </Form.Item>
                    </Input.Group>

                </Form.Item>
                <Form.Item
                    label="Receiver's account"
                    name="receiver"
                    rules={[{ required: true, message: 'Please choose an account' }]}
                >
                    <Select placeholder="Please choose an account">
                        {accounts.map((account) => (
                          <Select.Option key={account} value={account}>{account}</Select.Option>
                        ))}
                    </Select>
                </Form.Item>
                <Form.Item
                    label="Sender's private key"
                    rules={[{ required: true, message: 'Please choose at least one' }]}
                >
                    <Select
                      placeholder="custom dropdown render"
                      dropdownRender={(menu) => (
                        <>
                          {menu}
                          <Divider
                            style={{
                              margin: '8px 0',
                            }}
                          />
                          <Space
                            style={{
                              padding: '0 8px 4px',
                            }}
                          >
                            <Input
                              placeholder="Please enter item"
                              ref={inputRef}
                              value={name}
                              onChange={onNameChange}
                            />
                            <Button type="text" icon={<PlusOutlined />} onClick={addItem}>
                              Add item
                            </Button>
                          </Space>
                        </>
                      )}
                      options={items.map((item) => ({
                        label: item,
                        value: item,
                      }))}
                    />
                </Form.Item>


                <Button type="primary" htmlType="submit">Submit</Button>
            </Form>
        </>
    );
}