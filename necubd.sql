-- seciencia de autoincremento del ID_cliente
CREATE SEQUENCE cliente_id
    minvalue 1
	increment by 1;
	
CREATE SEQUENCE despacho_id
    minvalue 1
	increment by 1;

CREATE SEQUENCE producto_id
    minvalue 1
	increment by 1;
	
CREATE SEQUENCE pedido_id
    minvalue 1
	increment by 1;
	
CREATE SEQUENCE proveedor_id
    minvalue 1
	increment by 1;
	
CREATE SEQUENCE cod_id
    minvalue 1
	increment by 1;
	
CREATE SEQUENCE empleado_id
    minvalue 1
	increment by 1;
	
CREATE TABLE CLIENTE
(
    cliente_id INTEGER DEFAULT nextval('cliente_id') ,
    nombre     VARCHAR (30) NOT NULL ,
    apellido   VARCHAR (30) NOT NULL ,
    rut        VARCHAR (30) NOT NULL,
    direccion  VARCHAR (30) NOT NULL ,
    telefono   INTEGER
);



CREATE TABLE DESPACHO
(
    despacho_id   INTEGER DEFAULT nextval('despacho_id') ,
    fecha         DATE NOT NULL,
    hora_salida   TIME NOT NULL ,
    hora_entrega  TIME NOT NULL ,
    cliente_id    INTEGER NOT NULL,
    empleado_id   INTEGER NOT NULL
);
	  

CREATE TABLE PRODUCTO
( 
    producto_id INTEGER DEFAULT nextval('producto_id') ,
	nombre      VARCHAR(30) NOT NULL,
    descripcion VARCHAR(30),
    valor       INTEGER NOT NULL ,
    stock       INTEGER NOT NULL
);


CREATE TABLE PEDIDO
(
    codigo         INTEGER DEFAULT nextval('pedido_id') ,
    fecha          DATE NOT NULL ,
    total          INTEGER NOT NULL,
    cliente_id     INTEGER NOT NULL
);



CREATE TABLE FACTURA
(
    proveedor_id    INTEGER NOT NULL,
    producto_id     INTEGER NOT NULL,
	cod_pago        INTEGER NOT NULL,
    tipo_producto   VARCHAR(30) NOT NULL,
    monto_total     INTEGER NOT NULL
);



CREATE TABLE PROVEEDOR 
(
    proveedor_id    INTEGER DEFAULT nextval('proveedor_id'),
    producto_id     INTEGER NOT NULL
);



CREATE TABLE BOLETA
(
    cliente_id      INTEGER NOT NULL,
    detalle_venta   VARCHAR(50) NOT NULL,
    monto_neto      INTEGER NOT NULL,
    monto_iva       INTEGER NOT NULL,
    monto_total     INTEGER NOT NULL,
    fecha           DATE NOT NULL,
	cod_pago        INTEGER NOT NULL
);



CREATE TABLE PAGO
(
    estado          BOOLEAN NOT NULL,
    cod_pago        INTEGER DEFAULT nextval('cod_id')
);
 
CREATE TABLE EMPLEADO
(
    empleado_id     INTEGER DEFAULT nextval('empleado_id'),
	nombre          VARCHAR(30) NOT NULL,
	apellido        VARCHAR(30) NOT NULL,
	rut             VARCHAR(30) NOT NULL,
	sueldo          INTEGER NOT null
);



ALTER TABLE cliente add primary key(cliente_id);
ALTER TABLE despacho add primary key(despacho_id);
ALTER TABLE empleado add primary key (empleado_id);
ALTER TABLE proveedor add primary key (proveedor_id);
ALTER TABLE producto add primary key (producto_id);
ALTER TABLE pago add primary key(cod_pago);

ALTER TABLE despacho add foreign key (cliente_id) references cliente(cliente_id) on delete cascade;
ALTER TABLE despacho add foreign key (empleado_id) references empleado(empleado_id) on delete cascade;
ALTER TABLE boleta add foreign key(cliente_id) references cliente(cliente_id) on delete cascade;
ALTER TABLE boleta add foreign key(cod_pago) references pago(cod_pago) on delete cascade;
ALTER TABLE proveedor add foreign key(producto_id) references producto(producto_id) on delete cascade;
ALTER TABLE factura add foreign key(proveedor_id) references proveedor(proveedor_id) on delete cascade;
ALTER TABLE factura add foreign key(producto_id) references producto(producto_id) on delete cascade;
ALTER TABLE pedido add foreign key(cliente_id) references cliente(cliente_id) on delete cascade;
ALTER TABLE factura add foreign key(cod_pago) references pago(cod_pago) on delete cascade;

insert into empleado (nombre, apellido, rut, sueldo)
values('Pancho','Perez','111-1',500000);
insert into empleado (nombre, apellido, rut, sueldo)
values('Juan','Mondaca','222-2',750000);
insert into empleado (nombre, apellido, rut, sueldo)
values('Ana','Vasquez','333-3',850000);

insert into cliente (nombre, apellido, rut, direccion, telefono)
values('pedro', 'rojas', '2039-2', 'ong 7567',78545664);
insert into cliente (nombre, apellido, rut, direccion, telefono)
values('maite', 'sc', '256-7', 'ong 7567',45578564);

insert into despacho (fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
values('26-06-2022','08:20','10:30',2,1);
insert into despacho (fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
values('26-06-2022','08:40','10:00',2,2);
insert into despacho (fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
values('26-06-2022','08:30','12:00',2,1);

insert into producto (nombre,descripcion, valor, stock)
values('Jugo zuko','verde', 5000, 3);
insert into producto (nombre,descripcion, valor, stock)
values('Gatorade','azul', 7000, 10);
insert into producto (nombre,descripcion, valor, stock)
values('Platano','amarillo', 500, 20);

insert into pedido (fecha, total, cliente_id)
values ('26-06-2022', 30000, 2);
insert into pedido (fecha, total, cliente_id)
values ('26-06-2022', 48000, 2);
insert into pedido (fecha, total, cliente_id)
values ('26-06-2022', 48000, 2);

insert into proveedor(producto_id) values(1);
insert into proveedor(producto_id) values(3);
insert into proveedor(producto_id) values(2);
insert into proveedor(producto_id) values(2);

insert into pago(estado) values(false);
insert into pago(estado) values(false);
insert into pago(estado) values(true);
insert into pago(estado) values(true);

insert into factura(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total)
values(4,3,3,'Fruta',500);
insert into factura(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total)
values(1,3,3,'Fruta',500);
insert into factura(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total)
values(4,3,4,'Fruta',500);
insert into factura(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total)
values(2,3,4,'Gaseosa',7000);
insert into factura(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total)
values(2,2,1,'Gaseosa',7000);
insert into factura(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total)
values(4,3,1,'Gaseosa',7000);

select * from factura;
select * from proveedor;
select * from producto;
select * from pedido;
select * from despacho;
select * from pago;