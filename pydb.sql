/*
 Navicat Premium Data Transfer

 Source Server         : bj-cdb-d4zufg1y.sql.tencentcdb.com
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : bj-cdb-d4zufg1y.sql.tencentcdb.com:63799
 Source Schema         : pydb

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 17/09/2023 19:27:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES (1, '油站');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES (1, 1, 1);
INSERT INTO `auth_group_permissions` VALUES (2, 1, 2);
INSERT INTO `auth_group_permissions` VALUES (3, 1, 3);
INSERT INTO `auth_group_permissions` VALUES (4, 1, 4);
INSERT INTO `auth_group_permissions` VALUES (5, 1, 5);
INSERT INTO `auth_group_permissions` VALUES (6, 1, 6);
INSERT INTO `auth_group_permissions` VALUES (7, 1, 7);
INSERT INTO `auth_group_permissions` VALUES (8, 1, 8);
INSERT INTO `auth_group_permissions` VALUES (9, 1, 9);
INSERT INTO `auth_group_permissions` VALUES (10, 1, 10);
INSERT INTO `auth_group_permissions` VALUES (11, 1, 11);
INSERT INTO `auth_group_permissions` VALUES (12, 1, 12);
INSERT INTO `auth_group_permissions` VALUES (13, 1, 13);
INSERT INTO `auth_group_permissions` VALUES (14, 1, 14);
INSERT INTO `auth_group_permissions` VALUES (15, 1, 15);
INSERT INTO `auth_group_permissions` VALUES (16, 1, 16);
INSERT INTO `auth_group_permissions` VALUES (20, 1, 29);
INSERT INTO `auth_group_permissions` VALUES (21, 1, 30);
INSERT INTO `auth_group_permissions` VALUES (22, 1, 31);
INSERT INTO `auth_group_permissions` VALUES (23, 1, 32);
INSERT INTO `auth_group_permissions` VALUES (24, 1, 33);
INSERT INTO `auth_group_permissions` VALUES (25, 1, 34);
INSERT INTO `auth_group_permissions` VALUES (26, 1, 35);
INSERT INTO `auth_group_permissions` VALUES (27, 1, 36);
INSERT INTO `auth_group_permissions` VALUES (28, 1, 37);
INSERT INTO `auth_group_permissions` VALUES (29, 1, 38);
INSERT INTO `auth_group_permissions` VALUES (30, 1, 39);
INSERT INTO `auth_group_permissions` VALUES (31, 1, 40);

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add tc sport', 1, 'add_tcsport');
INSERT INTO `auth_permission` VALUES (2, 'Can change tc sport', 1, 'change_tcsport');
INSERT INTO `auth_permission` VALUES (3, 'Can delete tc sport', 1, 'delete_tcsport');
INSERT INTO `auth_permission` VALUES (4, 'Can view tc sport', 1, 'view_tcsport');
INSERT INTO `auth_permission` VALUES (5, 'Can add tc web', 2, 'add_tcweb');
INSERT INTO `auth_permission` VALUES (6, 'Can change tc web', 2, 'change_tcweb');
INSERT INTO `auth_permission` VALUES (7, 'Can delete tc web', 2, 'delete_tcweb');
INSERT INTO `auth_permission` VALUES (8, 'Can view tc web', 2, 'view_tcweb');
INSERT INTO `auth_permission` VALUES (9, 'Can add tc search', 3, 'add_tcsearch');
INSERT INTO `auth_permission` VALUES (10, 'Can change tc search', 3, 'change_tcsearch');
INSERT INTO `auth_permission` VALUES (11, 'Can delete tc search', 3, 'delete_tcsearch');
INSERT INTO `auth_permission` VALUES (12, 'Can view tc search', 3, 'view_tcsearch');
INSERT INTO `auth_permission` VALUES (13, 'Can add log entry', 4, 'add_logentry');
INSERT INTO `auth_permission` VALUES (14, 'Can change log entry', 4, 'change_logentry');
INSERT INTO `auth_permission` VALUES (15, 'Can delete log entry', 4, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (16, 'Can view log entry', 4, 'view_logentry');
INSERT INTO `auth_permission` VALUES (17, 'Can add permission', 5, 'add_permission');
INSERT INTO `auth_permission` VALUES (18, 'Can change permission', 5, 'change_permission');
INSERT INTO `auth_permission` VALUES (19, 'Can delete permission', 5, 'delete_permission');
INSERT INTO `auth_permission` VALUES (20, 'Can view permission', 5, 'view_permission');
INSERT INTO `auth_permission` VALUES (21, 'Can add group', 6, 'add_group');
INSERT INTO `auth_permission` VALUES (22, 'Can change group', 6, 'change_group');
INSERT INTO `auth_permission` VALUES (23, 'Can delete group', 6, 'delete_group');
INSERT INTO `auth_permission` VALUES (24, 'Can view group', 6, 'view_group');
INSERT INTO `auth_permission` VALUES (25, 'Can add user', 7, 'add_user');
INSERT INTO `auth_permission` VALUES (26, 'Can change user', 7, 'change_user');
INSERT INTO `auth_permission` VALUES (27, 'Can delete user', 7, 'delete_user');
INSERT INTO `auth_permission` VALUES (28, 'Can view user', 7, 'view_user');
INSERT INTO `auth_permission` VALUES (29, 'Can add content type', 8, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (30, 'Can change content type', 8, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (31, 'Can delete content type', 8, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (32, 'Can view content type', 8, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (33, 'Can add session', 9, 'add_session');
INSERT INTO `auth_permission` VALUES (34, 'Can change session', 9, 'change_session');
INSERT INTO `auth_permission` VALUES (35, 'Can delete session', 9, 'delete_session');
INSERT INTO `auth_permission` VALUES (36, 'Can view session', 9, 'view_session');
INSERT INTO `auth_permission` VALUES (37, 'Can add TcOneTwo两门三门', 10, 'add_tconetwo');
INSERT INTO `auth_permission` VALUES (38, 'Can change TcOneTwo两门三门', 10, 'change_tconetwo');
INSERT INTO `auth_permission` VALUES (39, 'Can delete TcOneTwo两门三门', 10, 'delete_tconetwo');
INSERT INTO `auth_permission` VALUES (40, 'Can view TcOneTwo两门三门', 10, 'view_tconetwo');
INSERT INTO `auth_permission` VALUES (41, 'Can add deng lu info', 18, 'add_dengluinfo');
INSERT INTO `auth_permission` VALUES (42, 'Can change deng lu info', 18, 'change_dengluinfo');
INSERT INTO `auth_permission` VALUES (43, 'Can delete deng lu info', 18, 'delete_dengluinfo');
INSERT INTO `auth_permission` VALUES (44, 'Can view deng lu info', 18, 'view_dengluinfo');
INSERT INTO `auth_permission` VALUES (45, 'Can add web info', 19, 'add_webinfo');
INSERT INTO `auth_permission` VALUES (46, 'Can change web info', 19, 'change_webinfo');
INSERT INTO `auth_permission` VALUES (47, 'Can delete web info', 19, 'delete_webinfo');
INSERT INTO `auth_permission` VALUES (48, 'Can view web info', 19, 'view_webinfo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$600000$KScVLxSliJCF2LosJAsjfb$SdcrVQ++ng5NsqeuOQ/RQBTys/4O7jx9thl0wZYpT0E=', '2023-09-17 11:23:50.359553', 1, 'admin', '', '', 'admin@qq.com', 1, 1, '2023-08-05 03:12:59.419078');
INSERT INTO `auth_user` VALUES (2, 'pbkdf2_sha256$600000$HKYVAE6Uu1OebDWyDntnvs$FIpDZb++PM4Yu1wTcxilOlzh0LpMxIaT4j6yA0NKM30=', '2023-08-12 02:02:30.588319', 0, 'dingkai', '', '', '', 1, 1, '2023-08-12 01:50:00.000000');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES (1, 2, 1);

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for dengluinfo
-- ----------------------------
DROP TABLE IF EXISTS `dengluinfo`;
CREATE TABLE `dengluinfo`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uid` int NULL DEFAULT NULL COMMENT '用户ID',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `passWord` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `remember_me` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'remember_me',
  `commit` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'commit',
  `utf8` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'utf8',
  `post1` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `post2` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `post3` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `token` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '获得的token信息',
  `status` int NOT NULL COMMENT '0 未开,1开',
  `created_at` datetime(6) NULL DEFAULT NULL,
  `updated_at` datetime(6) NULL DEFAULT NULL,
  `webid` int NULL DEFAULT NULL COMMENT '站点id',
  `cn_memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '中文备注',
  `type` smallint NULL DEFAULT NULL COMMENT ' 普通post',
  `cookie` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '获得的cookie信息',
  `authenticity_token` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '获得的authenticity_token信息',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '登录信息设置' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dengluinfo
-- ----------------------------
INSERT INTO `dengluinfo` VALUES (1, 1, '731772412@qq.com', 'dnjsrl0620', '1', '登录', NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, 0, NULL, 1, '_ga_4H2DFG8NDS=GS1.2.1694334350.1.1.1694334357.0.0.0;uu=4419892e-ffaa-497a-bdb2-87fefd3523d8;ref=TWVFM0VOS1pwL3lmTW9adEV4eGFNNjlsc3ZDUHUyNmFrWVZ5NzdVekRiTU5KMzkwUDJaTkdnK0dkd3duZVFxNUQ0UVU4Q0FyVHF6Y3NPQU0xb3NXWCtHYzQ3bkVDa3JkR0J4dWpsUUhQWEpNYm1VMGhqSWJOOEJTSDZVMi95T3UtLW1RVkJyVnZDZnAyeXpmczNQdWhqb2c9PQ%3D%3D--3fdeb6eaed3ddae1e03123cd90af2e34c39d073f;_gid=GA1.2.2053116155.1694334350;br=YkNrNGFGbjZzbk56cHB0N3RnV1N4TG1oV2VBRmxDZDVWeWdPUXZnL1NCeEVwOGtQMEszWFpiT055MzNvTnpIc0lvNTA1ZWZwbGZUYktKaEpFcDREUEhreUdKNVh0Q2l5enJ2WDhrQndlQ0tZWUIwelpZSlYvNEhoRVBqSzJRV3FEYzJ5SGNuL0RNVkpkWFdoYVV0Q01YOFcwNEpSbk9PRytvMlMwbFhQU2h1UlMrdnB5dytlcDlsSjU3RktwNFR5WGIzMjNhR1FjODg2RHdsM2FyZjdXYVUrSTJNRWMrOW0ycEJBM2NSNGx5Yz0tLWU4UHQ5Y0dBeDFlVWp3dXBJTldtZnc9PQ%3D%3D--5c8727d5c4417315b9b06c79e65c5daa21924c66;_ga=GA1.2.460005635.1694334350;stoken=28238905-c104eb008864f31a0d7e6c1d55a0a489152a19a4;remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaGJDRnNHYVFQcjl3RkpJaGxxZURZM2FVdENTSGhwYmxORGVWUk1la1ZFTlFZNkJrVlVTU0lYTVRZNU5ETXpORE0xTlM0eE5qQTVPRFUzQmpzQVJnPT0iLCJleHAiOiIyMDI2LTA5LTEwVDA4OjI1OjU1LjE2MVoiLCJwdXIiOm51bGx9fQ%3D%3D--c07f027b6a626808d65970f30520e3533d05fd7a;_gat_gtag_UA_1803143_12=1;_sp5=NVF2UGNYRWhmQXRydkhGNnREeEFWSkt1M2QyVlI5dXZoaitQVEpOVnNteVZLbWNLOFVwU1MyTXc3LzlvVjBoZjdmL25GR2t3eE9aN2hZS1loemZ2S0ZjOVVJekVJbW5UbHozbzM5R2FQc1hEZXo5Z3NjYkZJaGVnM3d2S2lURXl5VUhHOUNWSWVoNVZQNjVTMEg4a3pDVVFSWXpNNVpqbnB5ZmZidlpGd2s2ajJERUxhUWMwaHdkM1dpSzZ0Y3o5WE9DbjdySG5MMm5WOTNYbmVhbnRrY016OG5xby9BTHp2aFFtbU0yaUZ4ZklDUTlNemR6OElVWTlvZktoSS9OSlR0UlVDTmc3OE43T0w2cHpXRVV5ZksxRWh1aW5jakxOR1dKVDduV0VkMW1meHRDRFVBRzZ1bGJxQWhSbXBrRWZBVlZHVG5tL3Bvb21iLzRxdG9OMGVnU3lFdXpiclVkMzVoV1hHMldhWmRWTmR6U05GQWpyejA2TGlxRFNiOFdvLS1JUWZTSk4xNGdUZnh1M0krMUhMR3l3PT0%3D--abbd4a8e41f42a5e7d4af8d72810fa85ee6f2e09;ab=781;sstoken=28238905-c104eb008864f31a0d7e6c1d55a0a489152a19a4-28238906-4e89d217e64861bb66038d79da642d07226d2ca4;timezoneOffset=-480', 'lu19HDkgzPdFr-cUGrPX9So0YXHuCr2syAwVlxn-88R69Clko055CcpDuoq-070GPLre5mkanYj3AECUOMjlQg');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 88 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2023-08-05 03:16:16.118603', '1', 'no72', 1, '[{\"added\": {}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (2, '2023-08-05 03:16:48.716693', '1', '足球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (3, '2023-08-05 03:17:29.008824', '2', '大熊站', 1, '[{\"added\": {}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (4, '2023-08-05 08:05:05.522406', '2', '篮球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (5, '2023-08-06 04:45:35.236260', '1', '2', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (6, '2023-08-06 04:45:55.804904', '2', '3', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (7, '2023-08-12 01:50:05.236966', '2', 'dingkai', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (8, '2023-08-12 01:51:25.328860', '2', 'dingkai', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"User permissions\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (9, '2023-08-12 01:53:30.618170', '1', '油站', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (10, '2023-08-12 01:56:23.044414', '2', 'dingkai', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"User permissions\", \"Last login\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (11, '2023-08-12 01:57:57.930095', '1', '油站', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 6, 2);
INSERT INTO `django_admin_log` VALUES (12, '2023-08-12 01:59:14.567651', '2', 'dingkai', 2, '[{\"changed\": {\"fields\": [\"User permissions\", \"Last login\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (13, '2023-08-12 02:00:27.292218', '1', '油站', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (14, '2023-08-12 02:01:37.625043', '1', '油站', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 6, 2);
INSERT INTO `django_admin_log` VALUES (15, '2023-08-12 02:02:15.880905', '1', '油站', 2, '[]', 6, 1);
INSERT INTO `django_admin_log` VALUES (16, '2023-08-14 16:11:55.614568', '8', 'dk12', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (17, '2023-08-14 16:12:03.892320', '6', 'dk12', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (18, '2023-08-14 16:12:22.856382', '5', 'dk12', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (19, '2023-08-14 16:12:30.923422', '4', 'dk12', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (20, '2023-08-14 16:12:38.265100', '3', 'dk12', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (21, '2023-08-14 16:12:45.741034', '1', 'no72', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (22, '2023-08-14 16:15:01.612419', '2', '篮球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (23, '2023-08-14 22:59:12.100509', '8', '沙巴', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (24, '2023-08-14 22:59:32.653301', '7', '皇冠', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (25, '2023-08-14 22:59:53.704151', '6', '1xBet', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (26, '2023-08-14 23:00:22.665483', '5', 'Bet365', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (27, '2023-08-14 23:00:53.848047', '4', '韦德【威廉】', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (28, '2023-08-14 23:01:12.610981', '3', '大发体育', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (29, '2023-08-14 23:01:32.975794', '2', 'GGBet', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (30, '2023-08-14 23:01:56.440697', '1', '平博', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"Name\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (31, '2023-08-14 23:02:18.260619', '9', '利记', 1, '[{\"added\": {}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (32, '2023-08-14 23:02:40.482939', '10', '天宝博', 1, '[{\"added\": {}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (33, '2023-08-14 23:03:04.425086', '11', 'NewBB体育', 1, '[{\"added\": {}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (34, '2023-08-14 23:03:25.304481', '12', '易胜博', 1, '[{\"added\": {}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (35, '2023-08-14 23:04:08.832117', '2', '篮球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (36, '2023-08-14 23:04:20.081075', '1', '足球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (37, '2023-08-14 23:05:25.829424', '3', '网球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (38, '2023-08-14 23:06:56.886334', '4', '棒球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (39, '2023-08-14 23:07:32.420634', '5', '美式足球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (40, '2023-08-14 23:08:11.483404', '6', '英试橄榄球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (41, '2023-08-14 23:08:31.159098', '7', '手球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (42, '2023-08-14 23:08:47.270023', '8', '乒乓球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (43, '2023-08-14 23:09:15.485487', '9', '羽毛球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (44, '2023-08-14 23:09:37.387085', '10', '排球', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (45, '2023-08-14 23:09:55.665412', '11', '斯诺克', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (46, '2023-08-14 23:10:19.635300', '12', '飞镖', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (47, '2023-08-14 23:10:41.284329', '13', '反恐精英', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (48, '2023-08-14 23:11:09.105061', '14', '刀塔2', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (49, '2023-08-14 23:11:30.046064', '15', '王者荣耀', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (50, '2023-08-14 23:11:55.827406', '16', '英雄联盟', 1, '[{\"added\": {}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (51, '2023-08-14 23:34:40.775453', '16', '英雄联盟', 2, '[{\"changed\": {\"fields\": [\"\\u6bd4\\u8d5b\\u7c7b\\u578b\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (52, '2023-08-14 23:35:03.599332', '15', '王者荣耀', 2, '[{\"changed\": {\"fields\": [\"\\u6bd4\\u8d5b\\u7c7b\\u578b\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (53, '2023-08-14 23:35:10.479972', '14', '刀塔2', 2, '[{\"changed\": {\"fields\": [\"\\u6bd4\\u8d5b\\u7c7b\\u578b\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (54, '2023-08-14 23:35:17.637902', '13', '反恐精英', 2, '[{\"changed\": {\"fields\": [\"\\u6bd4\\u8d5b\\u7c7b\\u578b\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (55, '2023-08-15 15:51:44.267568', '1', '731772412@qq.com', 1, '[{\"added\": {}}]', 18, 1);
INSERT INTO `django_admin_log` VALUES (56, '2023-08-17 04:07:10.248123', '1', '平博', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (57, '2023-08-17 07:11:03.917744', '1', '731772412@qq.com', 2, '[{\"changed\": {\"fields\": [\"Cookie\"]}}]', 18, 1);
INSERT INTO `django_admin_log` VALUES (58, '2023-08-17 07:17:48.519577', '1', '731772412@qq.com', 2, '[{\"changed\": {\"fields\": [\"Cookie\"]}}]', 18, 1);
INSERT INTO `django_admin_log` VALUES (59, '2023-08-17 16:14:10.809920', '1', '731772412@qq.com', 2, '[{\"changed\": {\"fields\": [\"Remember me\", \"Commit\", \"Authenticity_token\"]}}]', 18, 1);
INSERT INTO `django_admin_log` VALUES (60, '2023-08-17 16:24:06.975467', '1', '731772412@qq.com', 2, '[{\"changed\": {\"fields\": [\"Authenticity_token\"]}}]', 18, 1);
INSERT INTO `django_admin_log` VALUES (61, '2023-08-21 08:32:23.354720', '5', 'Bet365', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (62, '2023-08-21 08:43:16.307415', '2', 'GGBet', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (63, '2023-08-21 08:55:56.672888', '4', '韦德【威廉】', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (64, '2023-08-21 08:58:42.231547', '5', 'Bet365', 2, '[]', 2, 1);
INSERT INTO `django_admin_log` VALUES (65, '2023-08-21 09:00:21.609257', '6', '1xBet', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (66, '2023-08-21 09:01:35.908280', '7', '皇冠', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (67, '2023-08-21 09:02:28.969776', '8', '沙巴', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (68, '2023-08-21 09:04:06.029302', '9', '利记', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (69, '2023-08-21 09:05:45.848839', '10', '天宝博', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (70, '2023-08-21 09:07:16.171116', '11', 'NewBB体育', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (71, '2023-08-21 09:08:28.805235', '12', '易胜博', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 2, 1);
INSERT INTO `django_admin_log` VALUES (72, '2023-08-21 09:11:57.218407', '1', '足球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (73, '2023-08-21 09:13:14.697441', '2', '篮球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (74, '2023-08-21 09:16:34.469663', '3', '网球', 2, '[{\"changed\": {\"fields\": [\"NoStr\", \"NoInt\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (75, '2023-08-21 09:19:17.195656', '4', '棒球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (76, '2023-08-21 09:20:17.293548', '5', '美式足球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (77, '2023-08-21 09:21:23.990056', '6', '英试橄榄球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (78, '2023-08-21 09:22:49.026355', '7', '手球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (79, '2023-08-21 09:26:20.551361', '8', '乒乓球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (80, '2023-08-21 09:28:43.887149', '9', '羽毛球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (81, '2023-08-21 09:30:12.030066', '10', '排球', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (82, '2023-08-21 09:31:02.247448', '11', '斯诺克', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (83, '2023-08-21 09:32:31.025738', '12', '飞镖', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (84, '2023-08-21 09:34:22.897189', '13', '反恐精英', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (85, '2023-08-21 09:36:06.126306', '14', '刀塔2', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (86, '2023-08-21 09:37:15.141102', '15', '王者荣耀', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);
INSERT INTO `django_admin_log` VALUES (87, '2023-08-21 09:38:26.933345', '16', '英雄联盟', 2, '[{\"changed\": {\"fields\": [\"NoStr\"]}}]', 1, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (4, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (18, 'app1', 'dengluinfo');
INSERT INTO `django_content_type` VALUES (10, 'app1', 'tconetwo');
INSERT INTO `django_content_type` VALUES (3, 'app1', 'tcsearch');
INSERT INTO `django_content_type` VALUES (1, 'app1', 'tcsport');
INSERT INTO `django_content_type` VALUES (2, 'app1', 'tcweb');
INSERT INTO `django_content_type` VALUES (19, 'app1', 'webinfo');
INSERT INTO `django_content_type` VALUES (6, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (5, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (7, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (8, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (11, 'kM', 'adapaybalancepay');
INSERT INTO `django_content_type` VALUES (12, 'kM', 'adapaycash');
INSERT INTO `django_content_type` VALUES (13, 'kM', 'commonuserstation2');
INSERT INTO `django_content_type` VALUES (14, 'kM', 'commonuserstationoiler');
INSERT INTO `django_content_type` VALUES (15, 'kM', 'oilgradeprice');
INSERT INTO `django_content_type` VALUES (16, 'kM', 'oilgun');
INSERT INTO `django_content_type` VALUES (17, 'kM', 'oilorder');
INSERT INTO `django_content_type` VALUES (9, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2023-08-05 03:05:18.876964');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2023-08-05 03:05:19.945093');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2023-08-05 03:05:20.217011');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2023-08-05 03:05:20.265996');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-05 03:05:20.312065');
INSERT INTO `django_migrations` VALUES (6, 'app1', '0001_initial', '2023-08-05 03:05:21.119998');
INSERT INTO `django_migrations` VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2023-08-05 03:05:21.359093');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2023-08-05 03:05:21.475612');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0003_alter_user_email_max_length', '2023-08-05 03:05:21.598164');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0004_alter_user_username_opts', '2023-08-05 03:05:21.647184');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0005_alter_user_last_login_null', '2023-08-05 03:05:21.749576');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0006_require_contenttypes_0002', '2023-08-05 03:05:21.792623');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2023-08-05 03:05:21.839552');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0008_alter_user_username_max_length', '2023-08-05 03:05:21.952529');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2023-08-05 03:05:22.070050');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0010_alter_group_name_max_length', '2023-08-05 03:05:22.177831');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0011_update_proxy_permissions', '2023-08-05 03:05:22.286180');
INSERT INTO `django_migrations` VALUES (18, 'auth', '0012_alter_user_first_name_max_length', '2023-08-05 03:05:22.401818');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2023-08-05 03:05:22.540279');
INSERT INTO `django_migrations` VALUES (20, 'app1', '0002_alter_tcsearch_tcsports_alter_tcsearch_tcwebs', '2023-08-05 04:49:01.454672');
INSERT INTO `django_migrations` VALUES (21, 'app1', '0003_alter_tcweb_options_alter_tcsearch_gender_and_more', '2023-08-06 04:29:43.014646');
INSERT INTO `django_migrations` VALUES (22, 'app1', '0004_alter_tcsearch_gender_alter_tcsearch_paixu', '2023-08-06 04:38:01.039131');
INSERT INTO `django_migrations` VALUES (23, 'app1', '0005_tconetwo_remove_tcsearch_menonetwo_and_more', '2023-08-06 04:43:45.744086');
INSERT INTO `django_migrations` VALUES (24, 'app1', '0006_rename_menonetwo_tcsearch_menonetwos_and_more', '2023-08-06 04:50:19.342551');
INSERT INTO `django_migrations` VALUES (25, 'app1', '0007_alter_tcsearch_paixu_alter_tcsearch_racetime', '2023-08-06 04:58:47.436074');
INSERT INTO `django_migrations` VALUES (26, 'app1', '0008_alter_tcsearch_gender_alter_tcsearch_paixu_and_more', '2023-08-06 05:11:53.716581');
INSERT INTO `django_migrations` VALUES (27, 'app1', '0009_alter_tcsearch_menonetwos_alter_tcsearch_paixu_and_more', '2023-08-06 11:47:04.816751');
INSERT INTO `django_migrations` VALUES (28, 'app1', '0010_tcsport_type_alter_tcsearch_gender_and_more', '2023-08-14 23:33:47.366752');
INSERT INTO `django_migrations` VALUES (29, 'app1', '0011_alter_tcsearch_gender_alter_tcsearch_paixu_and_more', '2023-08-14 23:49:13.137254');
INSERT INTO `django_migrations` VALUES (30, 'app1', '0012_dengluinfo_webinfo_alter_tcsearch_paixu_and_more', '2023-08-15 02:22:39.231181');
INSERT INTO `django_migrations` VALUES (31, 'app1', '0013_dengluinfo_cookie_alter_tcsearch_gender_and_more', '2023-08-15 15:24:09.299731');
INSERT INTO `django_migrations` VALUES (32, 'app1', '0014_alter_dengluinfo_cookie_alter_dengluinfo_type_and_more', '2023-08-15 15:47:29.275885');
INSERT INTO `django_migrations` VALUES (33, 'app1', '0015_alter_dengluinfo_cookie_alter_dengluinfo_token_and_more', '2023-08-15 15:50:13.827881');
INSERT INTO `django_migrations` VALUES (34, 'app1', '0016_dengluinfo_authenticity_token_alter_tcsearch_paixu_and_more', '2023-08-17 16:12:43.272503');
INSERT INTO `django_migrations` VALUES (35, 'app1', '0017_alter_tcsearch_paixu_alter_tcsearch_racetime_and_more', '2023-09-02 03:30:42.424838');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('1z8qzq6mstyrn7vbq8qu8jlyve8b8c97', '.eJzFlkuPmzAQgP8K4pwHD_PI3toeq1VPPZVVNNhD4i6YlQ2HapX_XhuQ2rgQ2GSzPdl4xh8zn4Hk1d1D2xz3rUK558x9cH139fdaDvQZhQmwnyAO9YbWopE835iUzRBVm8eaYfl5yD0DHEEd9e4wIMkOIUTfL4IQCIsDRABMIw-JV1AgIUSQMoKRVxAPk4T5RUzDXRoXAKyrqkLRKs368Zq5AirM3Acnc79WmbvSI9eV9SsFSKeANeWSltgHK1OfMuHzzZ8YvMAvJ4cSBEVHz9UCWivLPrYFVnGxfX7UEwMaOHq27TOBse8LknXasCGXCIzKtspHqp1t9bRybmzv9GTCyJmJ-p4XTCCpPtabVBnAAkld2p31LOnF9hLarC91VdXCMc-8oxpouL6oeYnySku04xncQOtgF41NbLmXvas7tl2SBeTgvTQGb1MYfKS-2SZtc5EN_cZL5yCB6XddcopXStOn2EE6xkVf55n3UvXGrmxL8SivFTfYacWsFp1yVx_z9dseEnvBt8FZ1qY5kG6gvh4iklI9xGGamiEh4b_3VOae6sixZGsom8s_uJqSREEHC8JkogHzTozrN_8rtiY8rf9PykL979P0iMqljdrHshtjISUTVXRfqzWtDxeUHWTdvsw463P-u7RFjVrKfM92mJ6e3NNvA6xyNg:1qUNWX:GLkl8GXfs4_8ei0NDs_SjDggHLrWc8E-dbe3i8diBeg', '2023-08-25 08:29:33.202470');
INSERT INTO `django_session` VALUES ('3jsnpkc5f64s0vezwukqwa7rgrzjneuz', '.eJzFlkuPmzAQgP8K4pwHD_PI3toeq1VPPZVVNNhD4i6YlQ2HapX_XhuQ2rgQ2GSzPdl4xh8zn4Hk1d1D2xz3rUK558x9cH139fdaDvQZhQmwnyAO9YbWopE835iUzRBVm8eaYfl5yD0DHEEd9e4wIMkOIUTfL4IQCIsDRABMIw-JV1AgIUSQMoKRVxAPk4T5RUzDXRoXAKyrqkLRKs368Zq5AirM3Acnc79WmbvSI9eV9SsFSKeANeWSltgHK1OfMuHzzZ8YvMAvJ4cSBEVHz9UCWivLPrYFVnGxfX7UEwMaOHq27TOBse8LknXasCGXCIzKtspHqp1t9bRybmzv9GTCyJmJ-p4XTCCpPtabVBnAAkld2p31LOnF9hLarC91VdXCMc-8oxpouL6oeYnySku04xncQOtgF41NbLmXvas7tl2SBeTgvTQGb1MYfKS-2SZtc5EN_cZL5yCB6XddcopXStOn2EE6xkVf55n3UvXGrmxL8SivFTfYacWsFp1yVx_z9dseEnvBt8FZ1qY5kG6gvh4iklI9xGGamiEh4b_3VOae6sixZGsom8s_uJqSREEHC8JkogHzTozrN_8rtiY8rf9PykL979P0iMqljdrHshtjISUTVXRfqzWtDxeUHWTdvsw463P-u7RFjVrKfM92mJ6e3NNvA6xyNg:1qUHBW:bYdab-bKhtkcs7275qvRGsTMjIcnlnz0YD-pIIjn6c8', '2023-08-25 01:43:26.193565');
INSERT INTO `django_session` VALUES ('429a9aca46p1ve9sa0ta3wqfqinvboqn', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qcdns:ifCj-Es5V6R0N_MpC8zEGwOUODFaCx9pu4464h4n9sw', '2023-09-17 03:29:36.674636');
INSERT INTO `django_session` VALUES ('5wr1q75d08t3jan5r6hxnkb70vu07chp', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qaQtz:0ffBcgsfRvKDTlmyAuoNnxsOkSCLnU4m_bV3ZMT2SmY', '2023-09-11 01:18:47.688957');
INSERT INTO `django_session` VALUES ('7fln010v5ijgd6tgb142nf439k74848i', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qcdgi:kKIIFOH88mg1Go6I6FA6IyHOJrv3mCLR4kPrGU0bXK8', '2023-09-17 03:22:12.166030');
INSERT INTO `django_session` VALUES ('8ht9zyax8admthk8ktnduoo7507u8bwn', '.eJzFVU1zmzAQ_SsMZ9t8CRC5tdNrb-30UDKeRVoMCQYGweSQ8X-vBCQTy9gQu56cZHafnva9XVmv5ha6Ntt2Apttzs0H0zFXH2MJsGcsVYI_QbmrNqwq2yZPNgqyGbNi87PiWHwfsUcEGYhM7vZcEkYIHjpO6npAeOAiAiD1bSR2yoB44APlBH07JTaGIXfSgHkRDVIA3le1x7ITkuvva2yWsMfYfDBi81tdO7G5kr9yWdsQS6ExUlizvGEFDsm9qlCo9PH2H1jujKIz8jKtxAKerimGnAV8n5cWyOMtLkmKTlFYAwo4_z0DlJARnDQInDXdPpmob4G8w8q4WtLhUaUx5yrr2Lark_1ihqirpr3am5b1-2eMeUPdz5WlQnRHvFOiOO7C1HfUAjyqi66B4np7XjCZNUdh7mnNFYp0n4jO-geT226VFL3gSr2h7mfPUiG6I75OJO0l6BK5RD7S_suOxq9bp6gqsX2Z8-oddj-zbtaouxjoAWfiSJoA6RemZtgnVE104FFVQBAS7_RMoc4UWY4FX0PRXn4k1L3w3Z7M9cIzAtRzd6ZF8jW0VPpCe94hC1vzf0RPWLlUqN4WOsWFjJypQpGINat2FyzbNVVXz3g2YL7ctEVCdcsiPRAO1PKuDhRK4UB7dFpfp7xSgW9ris6XMCr41JxLf1xHLZQG9JT7zNDr0z7XkZvUzAzwYgVaJ5ypP5lj4umWK8Y2Wxe5aKds-TjRX-vLgvJ1T1w9YB8ezcM_LAfPOA:1qY0EH:iKSSux2Ouku0SkHP5wALltA-zp8YDA7LdEMCqpaigKw', '2023-09-04 08:25:41.564157');
INSERT INTO `django_session` VALUES ('9bn007crdgd89zaktcwlzgy2ebp95hil', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qduSp:LdPYrJSW-tHMmfJRoGjpZuOMlC2VjrqcOl4C4tF-cWw', '2023-09-20 15:29:07.790832');
INSERT INTO `django_session` VALUES ('a9g1bwa2wht60552gb182di2b248d8xr', '.eJzFVU1zmzAQ_SsMZ9t8CRC5tdNrb-30UDKeRVoMCQYGweSQ8X-vBCQTy9gQu56cZHafnva9XVmv5ha6Ntt2Apttzs0H0zFXH2MJsGcsVYI_QbmrNqwq2yZPNgqyGbNi87PiWHwfsUcEGYhM7vZcEkYIHjpO6npAeOAiAiD1bSR2yoB44APlBH07JTaGIXfSgHkRDVIA3le1x7ITkuvva2yWsMfYfDBi81tdO7G5kr9yWdsQS6ExUlizvGEFDsm9qlCo9PH2H1jujKIz8jKtxAKerimGnAV8n5cWyOMtLkmKTlFYAwo4_z0DlJARnDQInDXdPpmob4G8w8q4WtLhUaUx5yrr2Lark_1ihqirpr3am5b1-2eMeUPdz5WlQnRHvFOiOO7C1HfUAjyqi66B4np7XjCZNUdh7mnNFYp0n4jO-geT226VFL3gSr2h7mfPUiG6I75OJO0l6BK5RD7S_suOxq9bp6gqsX2Z8-oddj-zbtaouxjoAWfiSJoA6RemZtgnVE104FFVQBAS7_RMoc4UWY4FX0PRXn4k1L3w3Z7M9cIzAtRzd6ZF8jW0VPpCe94hC1vzf0RPWLlUqN4WOsWFjJypQpGINat2FyzbNVVXz3g2YL7ctEVCdcsiPRAO1PKuDhRK4UB7dFpfp7xSgW9ris6XMCr41JxLf1xHLZQG9JT7zNDr0z7XkZvUzAzwYgVaJ5ypP5lj4umWK8Y2Wxe5aKds-TjRX-vLgvJ1T1w9YB8ezcM_LAfPOA:1qhptY:dk3-S7wkBzxs0gWZA0vUeIIV4a4sOKKSs68QAtiQ2xw', '2023-10-01 11:24:56.616120');
INSERT INTO `django_session` VALUES ('aevpmq5am83sx0mco90f0i6k478md280', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qYitO:ityRbs7yHuBBof8-TNIYJmK_wD_pB8q4H8JMX9iJF3I', '2023-09-06 08:07:06.420658');
INSERT INTO `django_session` VALUES ('dceasyszksbiwsvnuedjv47nvgw4rcyu', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qaTx9:iCdXyi_Mlx7N2kOkN6dDgPtT5A1hmNgxW6ZWEArrQp4', '2023-09-11 04:34:15.057828');
INSERT INTO `django_session` VALUES ('dj1rcqxoed57q6qe7ivls5kkq787id5k', '.eJzFVU1zmzAQ_SsMZ9t8CRC5tdNrb-30UDKeRVoMCQYGweSQ8X-vBCQTy9gQu56cZHafnva9XVmv5ha6Ntt2Apttzs0H0zFXH2MJsGcsVYI_QbmrNqwq2yZPNgqyGbNi87PiWHwfsUcEGYhM7vZcEkYIHjpO6npAeOAiAiD1bSR2yoB44APlBH07JTaGIXfSgHkRDVIA3le1x7ITkuvva2yWsMfYfDBi81tdO7G5kr9yWdsQS6ExUlizvGEFDsm9qlCo9PH2H1jujKIz8jKtxAKerimGnAV8n5cWyOMtLkmKTlFYAwo4_z0DlJARnDQInDXdPpmob4G8w8q4WtLhUaUx5yrr2Lark_1ihqirpr3am5b1-2eMeUPdz5WlQnRHvFOiOO7C1HfUAjyqi66B4np7XjCZNUdh7mnNFYp0n4jO-geT226VFL3gSr2h7mfPUiG6I75OJO0l6BK5RD7S_suOxq9bp6gqsX2Z8-oddj-zbtaouxjoAWfiSJoA6RemZtgnVE104FFVQBAS7_RMoc4UWY4FX0PRXn4k1L3w3Z7M9cIzAtRzd6ZF8jW0VPpCe94hC1vzf0RPWLlUqN4WOsWFjJypQpGINat2FyzbNVVXz3g2YL7ctEVCdcsiPRAO1PKuDhRK4UB7dFpfp7xSgW9ris6XMCr41JxLf1xHLZQG9JT7zNDr0z7XkZvUzAzwYgVaJ5ypP5lj4umWK8Y2Wxe5aKds-TjRX-vLgvJ1T1w9YB8ezcM_LAfPOA:1qZBxm:8koCc_G5iFqb9WDEYqkuXLmYSO4rrweRNL_TdEN1OE0', '2023-09-07 15:09:34.843491');
INSERT INTO `django_session` VALUES ('dj224ajv3gvaalyjqmqqwdzv4vws80vl', '.eJzFVU1zmzAQ_SsMZ9t8CRC5tdNrb-30UDKeRVoMCQYGweSQ8X-vBCQTy9gQu56cZHafnva9XVmv5ha6Ntt2Apttzs0H0zFXH2MJsGcsVYI_QbmrNqwq2yZPNgqyGbNi87PiWHwfsUcEGYhM7vZcEkYIHjpO6npAeOAiAiD1bSR2yoB44APlBH07JTaGIXfSgHkRDVIA3le1x7ITkuvva2yWsMfYfDBi81tdO7G5kr9yWdsQS6ExUlizvGEFDsm9qlCo9PH2H1jujKIz8jKtxAKerimGnAV8n5cWyOMtLkmKTlFYAwo4_z0DlJARnDQInDXdPpmob4G8w8q4WtLhUaUx5yrr2Lark_1ihqirpr3am5b1-2eMeUPdz5WlQnRHvFOiOO7C1HfUAjyqi66B4np7XjCZNUdh7mnNFYp0n4jO-geT226VFL3gSr2h7mfPUiG6I75OJO0l6BK5RD7S_suOxq9bp6gqsX2Z8-oddj-zbtaouxjoAWfiSJoA6RemZtgnVE104FFVQBAS7_RMoc4UWY4FX0PRXn4k1L3w3Z7M9cIzAtRzd6ZF8jW0VPpCe94hC1vzf0RPWLlUqN4WOsWFjJypQpGINat2FyzbNVVXz3g2YL7ctEVCdcsiPRAO1PKuDhRK4UB7dFpfp7xSgW9ris6XMCr41JxLf1xHLZQG9JT7zNDr0z7XkZvUzAzwYgVaJ5ypP5lj4umWK8Y2Wxe5aKds-TjRX-vLgvJ1T1w9YB8ezcM_LAfPOA:1qWfQQ:f1DqHZHEPtFAob5xtr4-SZ7GutA5orl2AxWz1ytYQFw', '2023-08-31 16:00:42.881257');
INSERT INTO `django_session` VALUES ('edzqc71z85yculrz7te4v1t58yk4qp3y', '.eJzFlkuPmzAQgP8K4pwHD_PI3toeq1VPPZVVNNhD4i6YlQ2HapX_XhuQ2rgQ2GSzPdl4xh8zn4Hk1d1D2xz3rUK558x9cH139fdaDvQZhQmwnyAO9YbWopE835iUzRBVm8eaYfl5yD0DHEEd9e4wIMkOIUTfL4IQCIsDRABMIw-JV1AgIUSQMoKRVxAPk4T5RUzDXRoXAKyrqkLRKs368Zq5AirM3Acnc79WmbvSI9eV9SsFSKeANeWSltgHK1OfMuHzzZ8YvMAvJ4cSBEVHz9UCWivLPrYFVnGxfX7UEwMaOHq27TOBse8LknXasCGXCIzKtspHqp1t9bRybmzv9GTCyJmJ-p4XTCCpPtabVBnAAkld2p31LOnF9hLarC91VdXCMc-8oxpouL6oeYnySku04xncQOtgF41NbLmXvas7tl2SBeTgvTQGb1MYfKS-2SZtc5EN_cZL5yCB6XddcopXStOn2EE6xkVf55n3UvXGrmxL8SivFTfYacWsFp1yVx_z9dseEnvBt8FZ1qY5kG6gvh4iklI9xGGamiEh4b_3VOae6sixZGsom8s_uJqSREEHC8JkogHzTozrN_8rtiY8rf9PykL979P0iMqljdrHshtjISUTVXRfqzWtDxeUHWTdvsw463P-u7RFjVrKfM92mJ6e3NNvA6xyNg:1qVCbs:XLE2tZIBAFY-3-QPe0vY15MtK1iv1aLWy2kzKJgn5as', '2023-08-27 15:02:28.376045');
INSERT INTO `django_session` VALUES ('exb2g7wht7y2pen1fb82nthi2lycubhv', '.eJzFlkuPmzAQgP8K4pwHD_PI3toeq1VPPZVVNNhD4i6YlQ2HapX_XhuQ2rgQ2GSzPdl4xh8zn4Hk1d1D2xz3rUK558x9cH139fdaDvQZhQmwnyAO9YbWopE835iUzRBVm8eaYfl5yD0DHEEd9e4wIMkOIUTfL4IQCIsDRABMIw-JV1AgIUSQMoKRVxAPk4T5RUzDXRoXAKyrqkLRKs368Zq5AirM3Acnc79WmbvSI9eV9SsFSKeANeWSltgHK1OfMuHzzZ8YvMAvJ4cSBEVHz9UCWivLPrYFVnGxfX7UEwMaOHq27TOBse8LknXasCGXCIzKtspHqp1t9bRybmzv9GTCyJmJ-p4XTCCpPtabVBnAAkld2p31LOnF9hLarC91VdXCMc-8oxpouL6oeYnySku04xncQOtgF41NbLmXvas7tl2SBeTgvTQGb1MYfKS-2SZtc5EN_cZL5yCB6XddcopXStOn2EE6xkVf55n3UvXGrmxL8SivFTfYacWsFp1yVx_z9dseEnvBt8FZ1qY5kG6gvh4iklI9xGGamiEh4b_3VOae6sixZGsom8s_uJqSREEHC8JkogHzTozrN_8rtiY8rf9PykL979P0iMqljdrHshtjISUTVXRfqzWtDxeUHWTdvsw463P-u7RFjVrKfM92mJ6e3NNvA6xyNg:1qUdxm:ValyvKy1ojUqiNucn0jYr8oBs5oSInyneL1IqRVQoeI', '2023-08-26 02:02:46.460053');
INSERT INTO `django_session` VALUES ('g0sug3m73l3qflrv1k61udifd8g00nq6', '.eJzFlk2PmzAQhv8K4pwPPsxH9tb2WK166qmsosEeEnfBrAwcqlX-e20TqY0LgU2W7Wkcz_hl3meIxau7h6497rsG5Z4z98H13dXfeznQZxQ6wX6CONQbWotW8nyjSzbnbLN5rBmWn8-1FwJHaI7qdBiQZIcQou8XQQiExQEiAKaRh8QrKJAQIkgZwcgriIdJwvwipuEujQsAZrqqUHSN0vrxmrkCKszcBydzv1aZu1KRq876nQKkU8CacklL7JOV7q_R6cvDnxi8wC8nhxIERUetmxlqnSz73BZYxcX2-VEttNBZR622fSUw9n1GsSo7H8glAqOyq_KBbietnlbOnfZOTzqNnOms73nBiCRVY70LlRaYAcmULYxnjhebS2hrfamrqhaOfuedpoWWqx81L1HeSIkaPS13VjNiV4mNHFmK3s2ObZZkhnLwXhiDtyEMPhLfpEmbXGSLfuOlc5DA1H9dcoo3QlNTNCJG4yqvy8qlUL3RlU0pHtTrxB10OjGJRZUsymO6f5tDMqRTS3bzHaVsmuNTLPqiJWnMcmHzSO0N35bOsi7NgZhAfRUiklIV4jBNdUhI-O8zG_3M5sixZGso2-sfIEoliQIjFoTJiAF9RwwPQX9nbXV6fAR_SmYO4H1MD6Cca9Qai-8NaSElI12Y23tN68MVZAdZdy8TzPqa_w5tllEbmW-_2rvTk3v6DQ8yx3c:1qUp40:SXvQUf-MrhI3QuzPZ-kYGTAJsGS5GyMzJcR7fbDTFiE', '2023-08-26 13:53:56.681006');
INSERT INTO `django_session` VALUES ('gwk4hc75q4v7w0bfr93gc2vdhwfkx8z0', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qaTzf:pfhM-7JyXAb0U-wEn-DcrlifENzSnmgDZx7UuThc8Ys', '2023-09-11 04:36:51.794014');
INSERT INTO `django_session` VALUES ('h53w4au4n1z1n00vbrrgfd5peno32opc', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qZ0MY:rIzoEQ5bLjDG9-z8LVhK43ljumVMuaU0XfB2LbB1xRU', '2023-09-07 02:46:22.366085');
INSERT INTO `django_session` VALUES ('hvqjns06lccndh20slp57nrmpfd9k7nc', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qcdSm:JrxeSNpTv5S5doBlkmeBH70Qlj6rjTKSlVw2LVrLteg', '2023-09-17 03:07:48.744511');
INSERT INTO `django_session` VALUES ('ivf2cqk7ej615gpp3pwaf3077bwn8y50', '.eJzFVU1zmzAQ_SsMZ9t8CRC5tdNrb-30UDKeRVoMCQYGweSQ8X-vBCQTy9gQu56cZHafnva9XVmv5ha6Ntt2Apttzs0H0zFXH2MJsGcsVYI_QbmrNqwq2yZPNgqyGbNi87PiWHwfsUcEGYhM7vZcEkYIHjpO6npAeOAiAiD1bSR2yoB44APlBH07JTaGIXfSgHkRDVIA3le1x7ITkuvva2yWsMfYfDBi81tdO7G5kr9yWdsQS6ExUlizvGEFDsm9qlCo9PH2H1jujKIz8jKtxAKerimGnAV8n5cWyOMtLkmKTlFYAwo4_z0DlJARnDQInDXdPpmob4G8w8q4WtLhUaUx5yrr2Lark_1ihqirpr3am5b1-2eMeUPdz5WlQnRHvFOiOO7C1HfUAjyqi66B4np7XjCZNUdh7mnNFYp0n4jO-geT226VFL3gSr2h7mfPUiG6I75OJO0l6BK5RD7S_suOxq9bp6gqsX2Z8-oddj-zbtaouxjoAWfiSJoA6RemZtgnVE104FFVQBAS7_RMoc4UWY4FX0PRXn4k1L3w3Z7M9cIzAtRzd6ZF8jW0VPpCe94hC1vzf0RPWLlUqN4WOsWFjJypQpGINat2FyzbNVVXz3g2YL7ctEVCdcsiPRAO1PKuDhRK4UB7dFpfp7xSgW9ris6XMCr41JxLf1xHLZQG9JT7zNDr0z7XkZvUzAzwYgVaJ5ypP5lj4umWK8Y2Wxe5aKds-TjRX-vLgvJ1T1w9YB8ezcM_LAfPOA:1qWto8:6vQEql422egmTtswLOAPxf7Tt5AenzNeNAD0eZJXYPQ', '2023-09-01 07:22:08.789904');
INSERT INTO `django_session` VALUES ('j94vw9tki5v82f91lrkcnkgj8w47qkc6', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qcc46:w7N6BlF7KGDzw6VbWboj3Bii7TfRSiVbHkXV4qWIIug', '2023-09-17 01:38:14.565354');
INSERT INTO `django_session` VALUES ('lh9ihcmrz4sshrejirxradg8m1vvf0vq', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qcdV6:-l19_T2asxhw9HNjdg-9Nop2jmIgxd7_UU0UNFgYv4c', '2023-09-17 03:10:12.452546');
INSERT INTO `django_session` VALUES ('mq3uwynilejreb6dw7kjhqtzyqdipy8y', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qfL2R:yblaPtIVMXmC-cB19lObMoHyACIa8y7Q6ZLY0OQvAU4', '2023-09-24 14:03:47.609966');
INSERT INTO `django_session` VALUES ('mqrk4v9jrbzxx4nzusq9xdgu3i977o99', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qe4nu:9kV2yWDzahtCOyuf5LcIumpOz-Ru6rDXDA8FemnPHCY', '2023-09-21 02:31:34.935827');
INSERT INTO `django_session` VALUES ('n7ei588emh9k85hlb3m2fujbk4f1cxrl', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qa5u8:P3w1SLeo1_mFiRgER6Jxa006i77NJAjRsCaWNCI6rmM', '2023-09-10 02:53:32.678075');
INSERT INTO `django_session` VALUES ('nyff8bs31c0wylsyfmddw2e9kbbtafph', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qfKLl:68oZ3X9w9LsUt5opBspsDpi5GzvfCm9R6xqJjfSrPuI', '2023-09-24 13:19:41.951343');
INSERT INTO `django_session` VALUES ('oin98bhe8rp6trr7boxvb7oidghi6ykn', '.eJzFU01vozAQ_SsR5yR8GTC9tffedk9LFQ22CWz5kg3aQ5X_vh6IVo0DgaZd9WRr3vjNvDfjN-sAfZcfeiXkoeDWg-Va2_exFNirqBHgv6E-NnvW1J0s0j2m7M-o2j83XJRP59wLghxUrl_7HoliAb5w3czzgfDQEwJA0MARxMkYEB8CoJyIwMmII6KIu1nI_JiGGQAfuqpE3SvN9estsWqoRGI9bBLrsW3dxNrqW6F7G2MZyE0GO1ZIVooRrLBDhfDl8x9so9pGdmoFRy_LEbOBV0Vtgy5td2x4b48pwPnPW1kaP2emUgBnsq_Sia5WiDptN3cJOb0gLAqOqOs43jVRkvRRFrh4AI_bspdQ3m_PH5EumoM5_9OaOxSZPvlmwDXLaHaaAhkOhrUCQrFy6FOKR0T865oKa6q8ECXfQdndXlbsP_AGMs-PZgTgt5sZiP6VNsI35vEvZeU4vkb0hJVrhZpjCaa4BCMzXSCJ2rHmeMOyo2z6dsGzMefbTVsl1LQsNANkpNafc6RAhSPtRbWhz6SPw8AxFM23cFbwoT3X_nguHpSG9Jp7ZunNbV-ayKfULCzwagXmJOgi8fTIkbHLd2Whuilb3m_09_qyon3Tk9gMRKcX6_QXoTC4cg:1qSEHW:n3-SOW7DICkdYpDOViWboruANx-jz1UVELDx8j5yq5U', '2023-08-19 10:13:10.997178');
INSERT INTO `django_session` VALUES ('okk5hva96zhp5h93j1p8oyxj79hbwir3', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qZhOG:DH2BIqAEEPY7s5sx9UiO8uEsIbzh2RvZb9uL86gqmdk', '2023-09-09 00:43:00.541549');
INSERT INTO `django_session` VALUES ('pbysf5vtpik7qck25r7fhd1z9knwxilo', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qaU3m:UlTYo4jokOSIHSFBexK0vI8qkkBDjw0NcAIdQEu46Ok', '2023-09-11 04:41:06.566725');
INSERT INTO `django_session` VALUES ('pgktwhyvt5vnjqa2y4siyxi8n8t679xs', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qarUW:rV3YPepFnBUzmwLxlvgA5XbrxyKs0glJ8YlN3lnHEvA', '2023-09-12 05:42:16.438041');
INSERT INTO `django_session` VALUES ('s55lr0wxwfxf8v40ep82t2r1ny3xoj54', '.eJzFVU1zmzAQ_SsMZ9t8CRC5tdNrb-30UDKeRVoMCQYGweSQ8X-vBCQTy9gQu56cZHafnva9XVmv5ha6Ntt2Apttzs0H0zFXH2MJsGcsVYI_QbmrNqwq2yZPNgqyGbNi87PiWHwfsUcEGYhM7vZcEkYIHjpO6npAeOAiAiD1bSR2yoB44APlBH07JTaGIXfSgHkRDVIA3le1x7ITkuvva2yWsMfYfDBi81tdO7G5kr9yWdsQS6ExUlizvGEFDsm9qlCo9PH2H1jujKIz8jKtxAKerimGnAV8n5cWyOMtLkmKTlFYAwo4_z0DlJARnDQInDXdPpmob4G8w8q4WtLhUaUx5yrr2Lark_1ihqirpr3am5b1-2eMeUPdz5WlQnRHvFOiOO7C1HfUAjyqi66B4np7XjCZNUdh7mnNFYp0n4jO-geT226VFL3gSr2h7mfPUiG6I75OJO0l6BK5RD7S_suOxq9bp6gqsX2Z8-oddj-zbtaouxjoAWfiSJoA6RemZtgnVE104FFVQBAS7_RMoc4UWY4FX0PRXn4k1L3w3Z7M9cIzAtRzd6ZF8jW0VPpCe94hC1vzf0RPWLlUqN4WOsWFjJypQpGINat2FyzbNVVXz3g2YL7ctEVCdcsiPRAO1PKuDhRK4UB7dFpfp7xSgW9ris6XMCr41JxLf1xHLZQG9JT7zNDr0z7XkZvUzAzwYgVaJ5ypP5lj4umWK8Y2Wxe5aKds-TjRX-vLgvJ1T1w9YB8ezcM_LAfPOA:1qZBwZ:aTZQFOzMAdSzLZyupt3mj7TZHMWphpgS1cWMCsPzmxU', '2023-09-07 15:08:19.864455');
INSERT INTO `django_session` VALUES ('s5w8o8ihchzsywq92wrgyj31nahome9b', '.eJzFU02PmzAQ_SuRz0nAYMDZ2_beW3sqq2iwh0CXj8gG9bDKf68NUbXxQmC7rfY01rzx87w34xdyhL4rjr1GdSwleSCUbF_nMhDP2FhA_oTm1O5F23SqzPa2ZH9F9f5rK7H6cq29IShAF-Z2GLDkgBAipXkQApNxgAiAPPKR-bkAFkIEXDKM_Jz5mCSS5rEIDzzOAeTQVY1Nrw3Xj5eUNFBjSh42KXk8n2lKtuZUmt7GXA5qk8NOlEpUOIK17VBb-Pb6N7HR51Z1egVHr6oR80DWZeOBedrrxHDfG0tAyu_3qgx-rcwUghSqr7OJrlaIumw3fyXk8mRhLKVFqe8HE0S_MPuAH-b2ohu25r96sUKC60ToJqjLm6Y9z4ANQVATIsaFCXHIuQ0JC9--qe2buiixkjuouvvraFiSKBjIgjCZEWA_1swEzL_zLHxnAH9KVvr_b0RPWLlWqDuWaIoLBZvpwpLonWhPdyw7qbY_L3g21ny6aauEupbFboKN1OY3jhRW4Uh789rQZ9of4sh3FM23cFXwrj03_gTUBs5j_pZ7ZundbV-ayIfULCzwagXuJPgi8fTILWNX7KpSd1O2vN7oz_VlRfuuJwc3kVyeyOU3g0-t0A:1qS9MV:bGlWYFScQeP-ZT2_91he5TJ36rwzWf3WKsm1veDU1wE', '2023-08-19 04:57:59.118813');
INSERT INTO `django_session` VALUES ('t21qnml82ae6xe2gwxa6898p1nj8ceej', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qaTQq:D0g35YnkVj21-S-tErM8OytxxfuNdp-bN1m48zsXNoI', '2023-09-11 04:00:52.635094');
INSERT INTO `django_session` VALUES ('tcu5t0y688tc4680y0wnd53mqc8b0l7p', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qVOFx:saSB0DzW0HHVCvLJ-McuW3jSbtwWd5ErY_dex8WuEzs', '2023-08-28 03:28:37.910698');
INSERT INTO `django_session` VALUES ('tptn68cjc31et6hr42q4i59oiirnj568', '.eJzFVE2PmzAQ_SsR5yRgMGD2tnvvrT2VVTTYQ6DlSxi0h1X-e21A1cYhgSZd7cngGb-Z997Y79YB-i479BLbQy6sJ4tY2497CfDfWOmA-AXVsd7zuuraPNnrlP0UlftvtcDiZco9A8hAZuq059IwQvCQkNT1gIrARQRA5jtInZQD9cAHJij6TkodDENB0oB7EQtSADF0VWLVS4X18z22Kigxtp42sfXcNCS2tuorV72Neym0mxR2PG95gWOw1B1KHT4__p1vZFO3nVyB0bfFGLNBlHllgyptd3w4b48pIMSPW1kqPmUmLYLgbV8mM12tIHXabu4icnrVYcyFjhLHcS-B4rgPU5_oBUTUFH0Lxf3yvGGyKI7O-Uxp7mBk6uSZqAqMokvVEvnIhj8nmv4e1ayusHurF2Wb0j5PuYc5mipSc4PMlGQJ0GHh2jGfMu1f4DHdQBBS77Km1DVllmMhdlB0t6-8ngLfHcBcL7xCQD9eVyxSb5utwzfs-Zuy0pr_Q3pGyrVETVuCOSzk9EoXGkTueH28IdmxrftmQbMx58tFW0XUlCw0N_wRWt3VEUIzHGHPqg19qisV-I7B6HoLE4N_mnOlj0v0wljALrGvDL057UuOPMRmYYBXMzCdiBaB5y3XiF22K3LZzcnycaK_VpcV7RuaEMcUiZ1erdMffDkfBQ:1qSVqw:X6NEtZrySb6w0sS-K3HMTjzM-0AiSehVzYzrX5uB-aE', '2023-08-20 04:58:54.067781');
INSERT INTO `django_session` VALUES ('ttbwlsaw9zujbnp3a924no2goawfxheq', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qd7F8:JIJplzie-he2lpmZftLAynIb5uz0UVVRk_Lhcj0Lkiw', '2023-09-18 10:55:42.249619');
INSERT INTO `django_session` VALUES ('wlp7mdxh8a2i7gcfrxvzh34s7bkz5hh4', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qdu9y:uvKu4Z7PKXIs7uYDz3iCvwFJeJBPkwFVtKO-qZrO3FE', '2023-09-20 15:09:38.711439');
INSERT INTO `django_session` VALUES ('x1od5qmsp5py7d1pc18bpuhtq7689ug9', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qenCa:Cb0mCoeSoSJPb_wSC8x7_jxDG_vVCwlLTKpGCjqD45s', '2023-09-23 01:56:00.054640');
INSERT INTO `django_session` VALUES ('xjvrc2vx8o73qi3tz0def2dhyruhhbmo', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qdlTu:ba-topWYzxuz7G3P3apfbKlBMF2OuPqXB2y4PnxQSSY', '2023-09-20 05:53:38.489380');
INSERT INTO `django_session` VALUES ('zexhv2nd5mnyvxnuaolzrj7k47rlvp3g', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qVOmC:AlEYzqs3p7HLueyuOmbTuhMI7J1I_ppKmoIKqjKjwRE', '2023-08-28 04:01:56.291652');
INSERT INTO `django_session` VALUES ('zjf5434sd04a1gy1e5j0h291l03c34y7', '.eJxVjDsOwjAUBO_iGll2_A0lPWewNn7POIASKU4qxN0hUgpod2b2JRK2taat8ZJGEmehxel3G5AfPO2A7phus8zztC7jIHdFHrTJ60z8vBzu30FFq9_adDb0DMNal87Aku-YAY5OsVUlwxo4RLLsVLGKQyBdfDZ99AUgLd4f8BA4gw:1qVPAR:ahXPVkzL6FT30FpslX07H_5jgBR_CeZQuI6Kx1edkwE', '2023-08-28 04:26:59.695690');

-- ----------------------------
-- Table structure for tconetwo
-- ----------------------------
DROP TABLE IF EXISTS `tconetwo`;
CREATE TABLE `tconetwo`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uid` int NULL DEFAULT NULL COMMENT '用户ID',
  `noStr` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'TcOneTwo编号str',
  `noInt` int NULL DEFAULT NULL COMMENT 'TcOneTwo编号int',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `status` int NOT NULL COMMENT '0 为开,1开',
  `created_at` datetime(6) NULL DEFAULT NULL,
  `updated_at` datetime(6) NULL DEFAULT NULL,
  `webid` int NULL DEFAULT NULL COMMENT '站点id',
  `cn_memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '中文备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'TcOneTwo各种站点信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tconetwo
-- ----------------------------
INSERT INTO `tconetwo` VALUES (1, NULL, '2', 2, '2', 1, NULL, NULL, 0, '两门');
INSERT INTO `tconetwo` VALUES (2, NULL, '3', 3, '3', 1, NULL, NULL, 0, '三门');

-- ----------------------------
-- Table structure for tcsearch
-- ----------------------------
DROP TABLE IF EXISTS `tcsearch`;
CREATE TABLE `tcsearch`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uid` int NULL DEFAULT NULL COMMENT '用户ID',
  `paiXu` smallint NULL DEFAULT NULL,
  `profitRangeLittle` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '利润范围最小值',
  `profitRangeBig` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '利润范围最大值',
  `returnOnInvestmentLittle` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '投资汇报率最小值',
  `returnOnInvestmentBig` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '投资汇报率最大值',
  `raceTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'raceTime比赛时间',
  `moreSearch` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '高级选项-多选内容',
  `status` int NOT NULL COMMENT '0 未开,1开',
  `created_at` datetime(6) NULL DEFAULT NULL,
  `updated_at` datetime(6) NULL DEFAULT NULL,
  `webid` int NULL DEFAULT NULL COMMENT '站点id',
  `cn_memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '中文备注',
  `gender` smallint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'TcSearch个人搜索条件' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tcsearch
-- ----------------------------
INSERT INTO `tcsearch` VALUES (1, 1, 3, '0', '2', '4', NULL, '604800', NULL, 1, '2023-08-05 12:32:23.000000', '2023-08-05 12:32:22.000000', 0, NULL, 2);
INSERT INTO `tcsearch` VALUES (2, 2, 1, '0', '0', '0', NULL, '1', NULL, 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsearch` VALUES (3, NULL, 3, '4', '2', '4', '5', NULL, NULL, 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsearch` VALUES (4, 99, 3, '', '', '', '', '', '', 1, NULL, NULL, NULL, '', NULL);
INSERT INTO `tcsearch` VALUES (5, 99, NULL, '', '', '', '', '', '', 1, NULL, NULL, NULL, '', NULL);
INSERT INTO `tcsearch` VALUES (6, 2, NULL, '', '', '', '', '', '', 1, NULL, NULL, NULL, '', NULL);

-- ----------------------------
-- Table structure for tcsearch_menonetwos
-- ----------------------------
DROP TABLE IF EXISTS `tcsearch_menonetwos`;
CREATE TABLE `tcsearch_menonetwos`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tcsearch_id` bigint NOT NULL,
  `tconetwo_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `TcSearch_menOneTwo_tcsearch_id_tconetwo_id_6d04a478_uniq`(`tcsearch_id` ASC, `tconetwo_id` ASC) USING BTREE,
  INDEX `TcSearch_menOneTwo_tconetwo_id_509badb9_fk_TcOneTwo_id`(`tconetwo_id` ASC) USING BTREE,
  CONSTRAINT `TcSearch_menOneTwo_tconetwo_id_509badb9_fk_TcOneTwo_id` FOREIGN KEY (`tconetwo_id`) REFERENCES `tconetwo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `TcSearch_menOneTwo_tcsearch_id_28516ef1_fk_TcSearch_id` FOREIGN KEY (`tcsearch_id`) REFERENCES `tcsearch` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tcsearch_menonetwos
-- ----------------------------
INSERT INTO `tcsearch_menonetwos` VALUES (1, 1, 1);
INSERT INTO `tcsearch_menonetwos` VALUES (3, 3, 1);

-- ----------------------------
-- Table structure for tcsearch_tcsports
-- ----------------------------
DROP TABLE IF EXISTS `tcsearch_tcsports`;
CREATE TABLE `tcsearch_tcsports`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tcsearch_id` bigint NOT NULL,
  `tcsport_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `TcSearch_tcSports_tcsearch_id_tcsport_id_a6c40411_uniq`(`tcsearch_id` ASC, `tcsport_id` ASC) USING BTREE,
  INDEX `TcSearch_tcSports_tcsport_id_e7aeec0b_fk_TcSports_id`(`tcsport_id` ASC) USING BTREE,
  CONSTRAINT `TcSearch_tcSports_tcsearch_id_399945de_fk_TcSearch_id` FOREIGN KEY (`tcsearch_id`) REFERENCES `tcsearch` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `TcSearch_tcSports_tcsport_id_e7aeec0b_fk_TcSports_id` FOREIGN KEY (`tcsport_id`) REFERENCES `tcsports` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 46 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tcsearch_tcsports
-- ----------------------------
INSERT INTO `tcsearch_tcsports` VALUES (37, 1, 1);
INSERT INTO `tcsearch_tcsports` VALUES (34, 1, 2);
INSERT INTO `tcsearch_tcsports` VALUES (35, 1, 3);
INSERT INTO `tcsearch_tcsports` VALUES (36, 1, 4);
INSERT INTO `tcsearch_tcsports` VALUES (38, 1, 5);
INSERT INTO `tcsearch_tcsports` VALUES (39, 1, 6);
INSERT INTO `tcsearch_tcsports` VALUES (40, 1, 7);
INSERT INTO `tcsearch_tcsports` VALUES (41, 1, 8);
INSERT INTO `tcsearch_tcsports` VALUES (42, 1, 9);
INSERT INTO `tcsearch_tcsports` VALUES (43, 1, 10);
INSERT INTO `tcsearch_tcsports` VALUES (44, 1, 11);

-- ----------------------------
-- Table structure for tcsearch_tcwebs
-- ----------------------------
DROP TABLE IF EXISTS `tcsearch_tcwebs`;
CREATE TABLE `tcsearch_tcwebs`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tcsearch_id` bigint NOT NULL,
  `tcweb_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `TcSearch_tcWebs_tcsearch_id_tcweb_id_4d58737d_uniq`(`tcsearch_id` ASC, `tcweb_id` ASC) USING BTREE,
  INDEX `TcSearch_tcWebs_tcweb_id_7c7c786f_fk_TcWeb_id`(`tcweb_id` ASC) USING BTREE,
  CONSTRAINT `TcSearch_tcWebs_tcsearch_id_2c4b1db8_fk_TcSearch_id` FOREIGN KEY (`tcsearch_id`) REFERENCES `tcsearch` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `TcSearch_tcWebs_tcweb_id_7c7c786f_fk_TcWeb_id` FOREIGN KEY (`tcweb_id`) REFERENCES `tcweb` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 79 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tcsearch_tcwebs
-- ----------------------------
INSERT INTO `tcsearch_tcwebs` VALUES (75, 1, 2);
INSERT INTO `tcsearch_tcwebs` VALUES (76, 1, 3);
INSERT INTO `tcsearch_tcwebs` VALUES (77, 1, 4);
INSERT INTO `tcsearch_tcwebs` VALUES (78, 1, 7);
INSERT INTO `tcsearch_tcwebs` VALUES (28, 3, 2);
INSERT INTO `tcsearch_tcwebs` VALUES (29, 3, 3);

-- ----------------------------
-- Table structure for tcsports
-- ----------------------------
DROP TABLE IF EXISTS `tcsports`;
CREATE TABLE `tcsports`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uid` int NULL DEFAULT NULL COMMENT '用户ID',
  `noStr` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'TcSports编号str',
  `noInt` int NULL DEFAULT NULL COMMENT 'TcSports编号int',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `status` int NOT NULL COMMENT '0 未开,1开',
  `created_at` datetime(6) NULL DEFAULT NULL,
  `updated_at` datetime(6) NULL DEFAULT NULL,
  `webid` int NULL DEFAULT NULL COMMENT '站点id',
  `cn_memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '中文备注',
  `type` smallint NULL DEFAULT NULL COMMENT ' 比赛类型',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'TcSports各种运动信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tcsports
-- ----------------------------
INSERT INTO `tcsports` VALUES (1, NULL, '15', NULL, '足球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (2, NULL, '4', NULL, '篮球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (3, NULL, '22', 22, '网球', 1, NULL, NULL, 1, NULL, 1);
INSERT INTO `tcsports` VALUES (4, NULL, '3', 1, '棒球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (5, NULL, '0', 1, '美式足球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (6, NULL, '20', 1, '英试橄榄球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (7, NULL, '17', NULL, '手球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (8, NULL, '23', NULL, '乒乓球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (9, NULL, '1', NULL, '羽毛球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (10, NULL, '24', 1, '排球', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (11, NULL, '21', 1, '斯诺克', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (12, NULL, '12', 1, '飞镖', 1, NULL, NULL, 0, NULL, 1);
INSERT INTO `tcsports` VALUES (13, NULL, '34', 2, '反恐精英', 1, NULL, NULL, 0, NULL, 2);
INSERT INTO `tcsports` VALUES (14, NULL, '39', 2, '刀塔2', 1, NULL, NULL, 0, NULL, 2);
INSERT INTO `tcsports` VALUES (15, NULL, '45', 2, '王者荣耀', 1, NULL, NULL, 0, NULL, 2);
INSERT INTO `tcsports` VALUES (16, NULL, '36', 2, '英雄联盟', 1, NULL, NULL, 0, NULL, 2);

-- ----------------------------
-- Table structure for tcweb
-- ----------------------------
DROP TABLE IF EXISTS `tcweb`;
CREATE TABLE `tcweb`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uid` int NULL DEFAULT NULL COMMENT '用户ID',
  `noStr` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'tcWeb编号str',
  `noInt` int NULL DEFAULT NULL COMMENT 'tcWeb编号int',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `status` int NOT NULL COMMENT '0 为开,1开',
  `created_at` datetime(6) NULL DEFAULT NULL,
  `updated_at` datetime(6) NULL DEFAULT NULL,
  `webid` int NULL DEFAULT NULL COMMENT '站点id',
  `cn_memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '中文备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'tcWeb各种站点信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tcweb
-- ----------------------------
INSERT INTO `tcweb` VALUES (1, NULL, '7', NULL, '平博', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (2, NULL, '175', 66, 'GGBet', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (3, NULL, '89', NULL, '大发体育', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (4, NULL, '55', NULL, '韦德【威廉】', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (5, NULL, '26', NULL, 'Bet365', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (6, NULL, '74', NULL, '1xBet', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (7, NULL, '66', NULL, '皇冠', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (8, NULL, '72', NULL, '沙巴', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (9, NULL, '25', NULL, '利记', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (10, NULL, '184', NULL, '天宝博', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (11, NULL, '110', NULL, 'NewBB体育', 1, NULL, NULL, 0, NULL);
INSERT INTO `tcweb` VALUES (12, NULL, '221', NULL, '易胜博', 1, NULL, NULL, 0, NULL);

-- ----------------------------
-- Table structure for webinfo
-- ----------------------------
DROP TABLE IF EXISTS `webinfo`;
CREATE TABLE `webinfo`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uid` int NULL DEFAULT NULL COMMENT '用户ID',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `webName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'webName',
  `domain` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'domain ',
  `status` int NOT NULL COMMENT '0 未开,1开',
  `created_at` datetime(6) NULL DEFAULT NULL,
  `updated_at` datetime(6) NULL DEFAULT NULL,
  `webid` int NULL DEFAULT NULL COMMENT '站点id',
  `cn_memo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '中文备注',
  `type` smallint NULL DEFAULT NULL COMMENT ' 类型',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '站点信息设置' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of webinfo
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
